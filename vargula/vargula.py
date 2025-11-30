"""
vargula - Simple cross-platform terminal text styling library with advanced color palette generation

Thread-safe class-based design with no global state.

Example:
    >>> vg = Vargula()
    >>> print(vg.style("Error", color="red", bg="white", look="bold"))
    >>> print(vg.style("Custom", color="#FF5733"))
    >>> vg.create("error", color="red", look="bold")
    >>> print(vg.format("An <error>error</error> occurred"))
    
    # Generate color palettes
    >>> palette = vg.generate_palette("#3498db", "complementary", 5)
    >>> theme = vg.generate_theme_palette("analogous", "#e74c3c")
    >>> vg.apply_palette_theme(theme)
"""


import sys
import os
import re
import random
import colorsys
import json
import time
from contextlib import contextmanager
from typing import List, Tuple, Dict, Literal, Optional
from pathlib import Path

# Type definitions
PaletteScheme = Literal[
    "monochromatic", "analogous", "complementary", 
    "triadic", "tetradic", "split_complementary", "square", "random"
]
ColorBlindType = Literal["protanopia", "deuteranopia", "tritanopia", "protanomaly", "deuteranomaly", "tritanomaly"]

# Color theory constants
ANALOGOUS_SPREAD = 60
TRIADIC_SPREAD = 120
TETRADIC_OFFSETS = [0, 60, 180, 240]
SQUARE_OFFSETS = [0, 90, 180, 270]
SPLIT_COMPLEMENTARY_OFFSETS = [0, 150, 210]

# ANSI color codes (foreground)
COLORS = {
    "black": 30, "red": 31, "green": 32, "yellow": 33,
    "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
    "bright_black": 90, "bright_red": 91, "bright_green": 92,
    "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
    "bright_cyan": 96, "bright_white": 97,
}

# ANSI background color codes
BG_COLORS = {
    "bg_black": 40, "bg_red": 41, "bg_green": 42, "bg_yellow": 43,
    "bg_blue": 44, "bg_magenta": 45, "bg_cyan": 46, "bg_white": 47,
    "bg_bright_black": 100, "bg_bright_red": 101, "bg_bright_green": 102,
    "bg_bright_yellow": 103, "bg_bright_blue": 104, "bg_bright_magenta": 105,
    "bg_bright_cyan": 106, "bg_bright_white": 107,
}

LOOKS = {
    "bold": 1, "dim": 2, "italic": 3, "underline": 4,
    "blink": 5, "reverse": 7, "hidden": 8, "strikethrough": 9,
}


class Vargula:
    """Main vargula styling class with complete functionality.
    
    Each instance maintains its own state (custom styles, themes, configuration)
    and is thread-safe when used independently.
    
    Example:
        >>> vg = Vargula()
        >>> print(vg.style("Hello", color="red", look="bold"))
        >>> vg.create("warning", color="yellow", look="bold")
        >>> print(vg.format("<warning>Warning!</warning>"))
    """
    __version__ = "2.0.0"
    def __init__(self, enabled: Optional[bool] = None):
        """Initialize a new Vargula instance.
        
        Args:
            enabled: Override automatic detection. If None, auto-detect based on
                    environment (NO_COLOR, FORCE_COLOR, tty status)
        """
        # Instance state
        self._custom_styles = {}
        self._predefined_styles = {}
        self._current_theme = {}
        
        # Configuration
        if enabled is None:
            self._enabled = self._auto_detect_support()
        else:
            self._enabled = enabled
            if enabled:
                self._init_windows()
        
        # Initialize predefined styles
        self._init_predefined_styles()
    
    def _auto_detect_support(self) -> bool:
        """Auto-detect if ANSI colors should be enabled."""
        if os.getenv("NO_COLOR"):
            return False
        
        if os.getenv("FORCE_COLOR"):
            self._init_windows()
            return True
        
        if hasattr(sys.stdout, "isatty") and not sys.stdout.isatty():
            return False
        
        self._init_windows()
        return True
    
    def _init_windows(self):
        """Enable ANSI support on Windows."""
        if sys.platform == "win32":
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                handle = kernel32.GetStdHandle(-11)
                mode = ctypes.c_ulong()
                kernel32.GetConsoleMode(handle, ctypes.byref(mode))
                mode.value |= 0x0004
                kernel32.SetConsoleMode(handle, mode)
            except Exception:
                pass
    
    def _init_predefined_styles(self):
        """Initialize predefined color and look tags."""
        for color_name in COLORS.keys():
            self._predefined_styles[color_name] = {"color": color_name, "bg": None, "look": None}
        
        for bg_name in BG_COLORS.keys():
            self._predefined_styles[bg_name] = {"color": None, "bg": bg_name, "look": None}
        
        for look_name in LOOKS.keys():
            self._predefined_styles[look_name] = {"color": None, "bg": None, "look": look_name}
    
    # ============================================
    # Color Conversion Utilities
    # ============================================
    
    @staticmethod
    def _hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:
            hex_color = ''.join([c*2 for c in hex_color])
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def _rgb_to_hex(r: int, g: int, b: int) -> str:
        """Convert RGB tuple to hex color."""
        return f"#{int(r):02x}{int(g):02x}{int(b):02x}"
    
    @staticmethod
    def _rgb_to_ansi(r: int, g: int, b: int, background: bool = False) -> str:
        """Convert RGB to ANSI 24-bit true color code."""
        prefix = 48 if background else 38
        return f"{prefix};2;{r};{g};{b}"
    
    def _parse_color(self, color, background: bool = False) -> Optional[str]:
        """Parse color input (name, hex, or RGB tuple) to ANSI code."""
        if not color:
            return None
        
        color_dict = BG_COLORS if background else COLORS
        color_key = f"bg_{color}" if background and not color.startswith("bg_") else color
        
        if color_key in color_dict:
            return str(color_dict[color_key])
        if color in color_dict:
            return str(color_dict[color])
        
        if isinstance(color, str) and color.startswith('#'):
            r, g, b = self._hex_to_rgb(color)
            return self._rgb_to_ansi(r, g, b, background)
        
        if isinstance(color, (tuple, list)) and len(color) == 3:
            return self._rgb_to_ansi(*color, background)
        
        return None
    
    @staticmethod
    def _hex_to_hsv(hex_color: str) -> Tuple[float, float, float]:
        """Convert hex color to HSV tuple (0-1 range)."""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
        return colorsys.rgb_to_hsv(r, g, b)
    
    @staticmethod
    def _hsv_to_hex(h: float, s: float, v: float) -> str:
        """Convert HSV (0-1 range) to hex color."""
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    
    @staticmethod
    def _rgb_to_relative_luminance(r: int, g: int, b: int) -> float:
        """Calculate relative luminance for WCAG contrast ratio."""
        def adjust(c):
            c = c / 255.0
            return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        
        return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)
    
    # ============================================
    # Core Styling Methods
    # ============================================
    
    def enable(self):
        """Enable styling for this instance."""
        self._enabled = True
    
    def disable(self):
        """Disable styling for this instance."""
        self._enabled = False
    
    def is_enabled(self) -> bool:
        """Check if styling is enabled."""
        return self._enabled
    
    def style(self, text: str, color=None, bg=None, look=None) -> str:
        """Apply color, background, and/or look to text.
        
        Args:
            text: Text to style
            color: Color name, hex string, or RGB tuple
            bg: Background color (name, hex, or RGB tuple)
            look: Look name or list of look names
            
        Returns:
            Styled text with ANSI codes (or plain text if disabled)
            
        Example:
            >>> vg = Vargula()
            >>> vg.style("Error", color="red", look="bold")
            >>> vg.style("Custom", color="#FF5733", bg="#000000")
        """
        if not self._enabled:
            return text
        
        codes = []
        
        fg_code = self._parse_color(color, background=False)
        if fg_code:
            codes.append(fg_code)
        
        bg_code = self._parse_color(bg, background=True)
        if bg_code:
            codes.append(bg_code)
        
        if look:
            if isinstance(look, str) and look in LOOKS:
                codes.append(str(LOOKS[look]))
            elif isinstance(look, (list, tuple)):
                for l in look:
                    if l in LOOKS:
                        codes.append(str(LOOKS[l]))
        
        if not codes:
            return text
        
        return f"\033[{';'.join(codes)}m{text}\033[0m"
    
    def create(self, name: str, color=None, bg=None, look=None):
        """Create a custom style tag for use in format().
        
        Args:
            name: Style name (used in tags like <name>text</name>)
            color: Color name, hex string, or RGB tuple
            bg: Background color
            look: Look name or list of look names
            
        Raises:
            ValueError: If name is empty or no styling specified
            
        Example:
            >>> vg = Vargula()
            >>> vg.create("error", color="red", look="bold")
            >>> vg.create("success", color="#2ecc71")
        """
        if not name:
            raise ValueError("Style name cannot be empty")
        
        if not color and not bg and not look:
            raise ValueError("Must specify at least color, bg, or look")
        
        self._custom_styles[name] = {"color": color, "bg": bg, "look": look}
    
    def delete(self, name: str) -> bool:
        """Delete a custom style tag.
        
        Args:
            name: Style name to delete
            
        Returns:
            True if style was deleted, False if not found
        """
        if name in self._custom_styles:
            del self._custom_styles[name]
            return True
        return False
    
    @staticmethod
    def strip(text: str) -> str:
        """Remove all markup tags from text.
        
        Args:
            text: Text with markup tags
            
        Returns:
            Text without tags
        """
        return re.sub(r'</?[\w_#-]+>', '', text)
    
    @staticmethod
    def clean(text: str) -> str:
        """Remove all ANSI escape codes from text.
        
        Args:
            text: Text with ANSI codes
            
        Returns:
            Plain text without ANSI codes
        """
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)
    
    @staticmethod
    def length(text: str) -> int:
        """Calculate the visible length of text (ignoring ANSI codes).
        
        Args:
            text: Text possibly containing ANSI codes
            
        Returns:
            Visible character count
        """
        return len(Vargula.clean(text))
    
    def set_theme(self, theme):
        """Set a theme with predefined styles.
        
        Args:
            theme: Either "dark", "light", or a dictionary of style definitions
            
        Example:
            >>> vg = Vargula()
            >>> vg.set_theme("dark")
            >>> vg.set_theme({
            ...     "error": {"color": "red", "look": "bold"},
            ...     "success": {"color": "green"}
            ... })
        """
        if isinstance(theme, str):
            if theme == "dark":
                theme = {
                    "error": {"color": "bright_red", "look": "bold"},
                    "success": {"color": "bright_green", "look": "bold"},
                    "warning": {"color": "bright_yellow", "look": "bold"},
                    "info": {"color": "bright_cyan"},
                    "debug": {"color": "bright_black"},
                    "critical": {"color": "white", "bg": "red", "look": "bold"},
                }
            elif theme == "light":
                theme = {
                    "error": {"color": "red", "look": "bold"},
                    "success": {"color": "green", "look": "bold"},
                    "warning": {"color": "yellow", "look": "bold"},
                    "info": {"color": "blue"},
                    "debug": {"color": "magenta"},
                    "critical": {"color": "white", "bg": "red", "look": "bold"},
                }
            else:
                raise ValueError(f"Unknown theme: {theme}")
        
        self._current_theme = theme
        
        for name, style_def in theme.items():
            self.create(name, **style_def)
    
    @contextmanager
    def temporary(self, name: str, color=None, bg=None, look=None):
        """Context manager for temporary custom styles.
        
        Args:
            name: Temporary style name
            color: Color
            bg: Background color
            look: Look style(s)
            
        Example:
            >>> vg = Vargula()
            >>> with vg.temporary("temp", color="cyan"):
            ...     print(vg.format("<temp>Temporary style</temp>"))
        """
        self.create(name, color=color, bg=bg, look=look)
        try:
            yield
        finally:
            self.delete(name)
    
    def format(self, text: str) -> str:
        """Format text with markup-style tags, handling escape sequences.
        
        Escape sequences: Use \\< to show literal < character
        
        Supports:
        - Named styles: <red>text</red>, <bold>text</bold>
        - Hex foreground: <#FF5733>text</#FF5733>
        - Hex background: <@#FF5733>text</@#FF5733>
        - Named background: <@red>text</@red>
        - Combined: <#FFFFFF><@#000000>text</@#000000></#FFFFFF>
        - Nesting: <red><bold>text</bold></red>
        
        Args:
            text: Text with markup tags
            
        Returns:
            Formatted text with ANSI codes
            
        Example:
            >>> vg = Vargula()
            >>> vg.create("error", color="red", look="bold")
            >>> vg.format("<error>Error:</error> Something went wrong")
            >>> vg.format("<#FF5733>Custom hex color</#FF5733>")
        """
        if not self._enabled:
            return self.strip(text)
        
        ESCAPE_PLACEHOLDER = "\x00ESCAPED_LT\x00"
        ESCAPE_GT_PLACEHOLDER = "\x00ESCAPED_GT\x00"
        text = text.replace(r'\<', ESCAPE_PLACEHOLDER)
        text = text.replace(r'\>', ESCAPE_GT_PLACEHOLDER)
        
        all_styles = {**self._predefined_styles, **self._current_theme, **self._custom_styles}
        
        def find_close_tag(text, start_pos, tag_name):
            """Find matching closing tag position, accounting for nesting."""
            open_tag = f"<{tag_name}>"
            close_tag = f"</{tag_name}>"
            depth = 1
            i = start_pos
            
            while i < len(text) and depth > 0:
                if text[i:i + len(open_tag)] == open_tag:
                    depth += 1
                    i += len(open_tag)
                elif text[i:i + len(close_tag)] == close_tag:
                    depth -= 1
                    if depth == 0:
                        return i
                    i += len(close_tag)
                else:
                    i += 1
            
            return -1
        
        def collect_style_codes(color=None, bg=None, look=None):
            """Collect ANSI codes without wrapping text."""
            codes = []
            
            fg_code = self._parse_color(color, background=False)
            if fg_code:
                codes.append(fg_code)
            
            bg_code = self._parse_color(bg, background=True)
            if bg_code:
                codes.append(bg_code)
            
            if look:
                if isinstance(look, str) and look in LOOKS:
                    codes.append(str(LOOKS[look]))
                elif isinstance(look, (list, tuple)):
                    for l in look:
                        if l in LOOKS:
                            codes.append(str(LOOKS[l]))
            
            return codes
        
        def process_text(text, inherited_codes=None):
            """Process text and handle nested tags with inherited styles."""
            if inherited_codes is None:
                inherited_codes = []
            
            result = []
            i = 0
            
            while i < len(text):
                if text[i] == '<' and i + 1 < len(text) and text[i + 1] != '/':
                    match = re.match(r'<(@?#?[\w_#-]+)>', text[i:])
                    if match:
                        tag_name = match.group(1)
                        content_start = i + match.end()
                        close_pos = find_close_tag(text, content_start, tag_name)
                        
                        is_hex_fg = tag_name.startswith('#')
                        is_hex_bg = tag_name.startswith('@#')
                        is_named_bg = tag_name.startswith('@') and not is_hex_bg
                        is_named_style = tag_name in all_styles
                        
                        if close_pos != -1 and (is_hex_fg or is_hex_bg or is_named_bg or is_named_style):
                            if is_hex_fg:
                                new_codes = collect_style_codes(color=tag_name)
                            elif is_hex_bg:
                                bg_color = '#' + tag_name[2:]
                                new_codes = collect_style_codes(bg=bg_color)
                            elif is_named_bg:
                                color_name = tag_name[1:]
                                new_codes = collect_style_codes(bg=color_name)
                            else:
                                style_def = all_styles[tag_name]
                                new_codes = collect_style_codes(
                                    color=style_def.get("color"),
                                    bg=style_def.get("bg"),
                                    look=style_def.get("look")
                                )
                            
                            combined_codes = inherited_codes + new_codes
                            inner_text = text[content_start:close_pos]
                            processed_inner = process_text(inner_text, combined_codes)
                            
                            if combined_codes:
                                styled = f"\033[{';'.join(combined_codes)}m{processed_inner}\033[0m"
                                if inherited_codes:
                                    styled += f"\033[{';'.join(inherited_codes)}m"
                            else:
                                styled = processed_inner
                            
                            result.append(styled)
                            i = close_pos + len(f"</{tag_name}>")
                            continue
                
                result.append(text[i])
                i += 1
            
            return ''.join(result)
        
        formatted = process_text(text)
        formatted = formatted.replace(ESCAPE_PLACEHOLDER, '<')
        formatted = formatted.replace(ESCAPE_GT_PLACEHOLDER, '>')
        
        return formatted
    
    def write(self, *args, sep=" ", end="\n", file=None, flush=False):
        """Print formatted text with markup-style tags (works like built-in print()).
        
        Args:
            *args: Values to print (will be converted to strings and formatted)
            sep: String inserted between values (default: single space)
            end: String appended after the last value (default: newline)
            file: File object; defaults to sys.stdout
            flush: Whether to forcibly flush the stream
        
        Example:
            >>> vg = Vargula()
            >>> vg.create("error", color="red", look="bold")
            >>> vg.write("<error>Error:</error>", "File not found", sep=" - ")
        """
        if file is None:
            file = sys.stdout
        
        formatted_args = [self.format(str(arg)) for arg in args]
        output = sep.join(formatted_args)
        print(output, end=end, file=file, flush=flush)

    # ============================================
    # Color Manipulation Methods
    # ============================================
    
    def lighten(self, color: str, amount: float = 0.1) -> str:
        """Increase brightness (value) of a color.
        
        Args:
            color: Hex color to lighten
            amount: Amount to increase value (0-1)
            
        Returns:
            Lightened hex color
        """
        h, s, v = self._hex_to_hsv(color)
        v = min(1.0, v + amount)
        return self._hsv_to_hex(h, s, v)
    
    def darken(self, color: str, amount: float = 0.1) -> str:
        """Decrease brightness (value) of a color.
        
        Args:
            color: Hex color to darken
            amount: Amount to decrease value (0-1)
            
        Returns:
            Darkened hex color
        """
        h, s, v = self._hex_to_hsv(color)
        v = max(0.0, v - amount)
        return self._hsv_to_hex(h, s, v)
    
    def saturate(self, color: str, amount: float = 0.1) -> str:
        """Increase saturation of a color.
        
        Args:
            color: Hex color to saturate
            amount: Amount to increase saturation (0-1)
            
        Returns:
            More saturated hex color
        """
        h, s, v = self._hex_to_hsv(color)
        s = min(1.0, s + amount)
        return self._hsv_to_hex(h, s, v)
    
    def desaturate(self, color: str, amount: float = 0.1) -> str:
        """Decrease saturation of a color.
        
        Args:
            color: Hex color to desaturate
            amount: Amount to decrease saturation (0-1)
            
        Returns:
            Less saturated hex color
        """
        h, s, v = self._hex_to_hsv(color)
        s = max(0.0, s - amount)
        return self._hsv_to_hex(h, s, v)
    
    def shift_hue(self, color: str, degrees: float) -> str:
        """Rotate hue by specified degrees.
        
        Args:
            color: Hex color to shift
            degrees: Degrees to rotate hue (-360 to 360)
            
        Returns:
            Hue-shifted hex color
        """
        h, s, v = self._hex_to_hsv(color)
        h = (h + degrees / 360) % 1.0
        return self._hsv_to_hex(h, s, v)
    
    def invert(self, color: str) -> str:
        """Invert a color.
        
        Args:
            color: Hex color to invert
            
        Returns:
            Inverted hex color
        """
        r, g, b = self._hex_to_rgb(color)
        return self._rgb_to_hex(255 - r, 255 - g, 255 - b)
    
    def mix(self, color1: str, color2: str, weight: float = 0.5) -> str:
        """Mix two colors together.
        
        Args:
            color1: First hex color
            color2: Second hex color
            weight: Weight of first color (0-1, default 0.5 for equal mix)
            
        Returns:
            Mixed hex color
        """
        r1, g1, b1 = self._hex_to_rgb(color1)
        r2, g2, b2 = self._hex_to_rgb(color2)
        
        r = int(r1 * weight + r2 * (1 - weight))
        g = int(g1 * weight + g2 * (1 - weight))
        b = int(b1 * weight + b2 * (1 - weight))
        
        return self._rgb_to_hex(r, g, b)
    
    # ============================================
    # Accessibility Methods
    # ============================================
    
    def calculate_contrast_ratio(self, color1: str, color2: str) -> float:
        """Calculate WCAG 2.1 contrast ratio between two colors.
        
        Args:
            color1: First hex color
            color2: Second hex color
            
        Returns:
            Contrast ratio (1-21, where 21 is maximum contrast)
        """
        r1, g1, b1 = self._hex_to_rgb(color1)
        r2, g2, b2 = self._hex_to_rgb(color2)
        
        l1 = self._rgb_to_relative_luminance(r1, g1, b1)
        l2 = self._rgb_to_relative_luminance(r2, g2, b2)
        
        lighter = max(l1, l2)
        darker = min(l1, l2)
        
        return (lighter + 0.05) / (darker + 0.05)
    
    def meets_wcag(self, color1: str, color2: str, level: str = "AA", large_text: bool = False) -> bool:
        """Check if color pair meets WCAG contrast requirements.
        
        Args:
            color1: First hex color (e.g., text color)
            color2: Second hex color (e.g., background color)
            level: WCAG level - "AA" or "AAA"
            large_text: True if text is 18pt+ or 14pt+ bold
            
        Returns:
            True if colors meet the specified WCAG level
        """
        ratio = self.calculate_contrast_ratio(color1, color2)
        
        if level == "AAA":
            required = 4.5 if large_text else 7.0
        else:  # AA
            required = 3.0 if large_text else 4.5
        
        return ratio >= required
    
    def ensure_contrast(self, foreground: str, background: str, min_ratio: float = 4.5, 
                       max_iterations: int = 20) -> str:
        """Adjust foreground color to meet minimum contrast ratio.
        
        Args:
            foreground: Foreground hex color to adjust
            background: Background hex color
            min_ratio: Minimum contrast ratio to achieve
            max_iterations: Maximum adjustment attempts
            
        Returns:
            Adjusted foreground color that meets contrast requirement
        """
        current_ratio = self.calculate_contrast_ratio(foreground, background)
        
        if current_ratio >= min_ratio:
            return foreground
        
        h, s, v = self._hex_to_hsv(foreground)
        bg_h, bg_s, bg_v = self._hex_to_hsv(background)
        
        should_lighten = bg_v < 0.5
        
        for _ in range(max_iterations):
            if should_lighten:
                v = min(1.0, v + 0.05)
            else:
                v = max(0.0, v - 0.05)
            
            adjusted = self._hsv_to_hex(h, s, v)
            current_ratio = self.calculate_contrast_ratio(adjusted, background)
            
            if current_ratio >= min_ratio:
                return adjusted
        
        return "#ffffff" if should_lighten else "#000000"
    
    # ============================================
    # Color Blindness Simulation
    # ============================================
    
    def simulate_colorblindness(self, hex_color: str, cb_type: ColorBlindType) -> str:
        """Simulate how a color appears to colorblind individuals.
        
        Args:
            hex_color: Input hex color
            cb_type: Type of color blindness
            
        Returns:
            Hex color as it would appear
        """
        r, g, b = self._hex_to_rgb(hex_color)
        
        matrices = {
            "protanopia": [
                [0.567, 0.433, 0.000],
                [0.558, 0.442, 0.000],
                [0.000, 0.242, 0.758]
            ],
            "deuteranopia": [
                [0.625, 0.375, 0.000],
                [0.700, 0.300, 0.000],
                [0.000, 0.300, 0.700]
            ],
            "tritanopia": [
                [0.950, 0.050, 0.000],
                [0.000, 0.433, 0.567],
                [0.000, 0.475, 0.525]
            ],
            "protanomaly": [
                [0.817, 0.183, 0.000],
                [0.333, 0.667, 0.000],
                [0.000, 0.125, 0.875]
            ],
            "deuteranomaly": [
                [0.800, 0.200, 0.000],
                [0.258, 0.742, 0.000],
                [0.000, 0.142, 0.858]
            ],
            "tritanomaly": [
                [0.967, 0.033, 0.000],
                [0.000, 0.733, 0.267],
                [0.000, 0.183, 0.817]
            ]
        }
        
        if cb_type not in matrices:
            return hex_color
        
        matrix = matrices[cb_type]
        
        new_r = matrix[0][0] * r + matrix[0][1] * g + matrix[0][2] * b
        new_g = matrix[1][0] * r + matrix[1][1] * g + matrix[1][2] * b
        new_b = matrix[2][0] * r + matrix[2][1] * g + matrix[2][2] * b
        
        new_r = max(0, min(255, int(new_r)))
        new_g = max(0, min(255, int(new_g)))
        new_b = max(0, min(255, int(new_b)))
        
        return self._rgb_to_hex(new_r, new_g, new_b)
    
    def validate_colorblind_safety(self, colors: List[str], cb_type: ColorBlindType = "deuteranopia",
                                   min_difference: float = 30) -> Tuple[bool, List[Tuple[int, int]]]:
        """Check if palette colors are distinguishable for colorblind users.
        
        Args:
            colors: List of hex colors to validate
            cb_type: Type of color blindness to test
            min_difference: Minimum perceptual difference required
            
        Returns:
            Tuple of (is_safe, list of problematic color pair indices)
        """
        simulated = [self.simulate_colorblindness(c, cb_type) for c in colors]
        problems = []
        
        for i in range(len(simulated)):
            for j in range(i + 1, len(simulated)):
                r1, g1, b1 = self._hex_to_rgb(simulated[i])
                r2, g2, b2 = self._hex_to_rgb(simulated[j])
                
                distance = ((r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2) ** 0.5
                
                if distance < min_difference:
                    problems.append((i, j))
        
        return len(problems) == 0, problems
    
    # ============================================
    # Palette Generation Methods
    # ============================================
    
    def generate_palette(
        self,
        base_color: str = None,
        scheme: PaletteScheme = "random",
        count: int = 5,
        saturation_range: Tuple[float, float] = (0.4, 0.9),
        value_range: Tuple[float, float] = (0.5, 0.95),
        randomize: bool = True
    ) -> List[str]:
        """Generate a color palette based on color theory.
        
        Args:
            base_color: Starting hex color. If None, random.
            scheme: Color harmony scheme to use
            count: Number of colors to generate
            saturation_range: (min, max) saturation values (0-1)
            value_range: (min, max) brightness values (0-1)
            randomize: Add slight random variations
            
        Returns:
            List of hex color strings
        """
        if base_color is None:
            h = random.random()
            s = random.uniform(*saturation_range)
            v = random.uniform(*value_range)
        else:
            h, s, v = self._hex_to_hsv(base_color)
        
        colors = []
        
        if scheme == "monochromatic":
            colors.append(self._hsv_to_hex(h, s, v))
            for i in range(1, count):
                new_s = s * (0.6 + 0.8 * i / count)
                new_v = v * (0.7 + 0.6 * i / count)
                if randomize:
                    new_s += random.uniform(-0.1, 0.1)
                    new_v += random.uniform(-0.1, 0.1)
                new_s = max(0.2, min(1.0, new_s))
                new_v = max(0.3, min(1.0, new_v))
                colors.append(self._hsv_to_hex(h, new_s, new_v))

        elif scheme == "analogous":
            step = ANALOGOUS_SPREAD / max(count - 1, 1)
            for i in range(count):
                offset = -30 + i * step
                if randomize:
                    offset += random.uniform(-5, 5)
                new_h = (h + offset / 360) % 1.0
                new_s = s + random.uniform(-0.1, 0.1) if randomize else s
                new_v = v + random.uniform(-0.1, 0.1) if randomize else v
                new_s = max(0.3, min(1.0, new_s))
                new_v = max(0.4, min(1.0, new_v))
                colors.append(self._hsv_to_hex(new_h, new_s, new_v))
        
        elif scheme == "complementary":
            colors.append(self._hsv_to_hex(h, s, v))
            complement_h = (h + 0.5) % 1.0
            colors.append(self._hsv_to_hex(complement_h, s, v))
            
            for i in range(2, count):
                use_base = i % 2 == 0
                base_h = h if use_base else complement_h
                offset = random.uniform(-0.1, 0.1) if randomize else 0
                new_h = (base_h + offset) % 1.0
                new_s = s + random.uniform(-0.15, 0.15) if randomize else s
                new_v = v + random.uniform(-0.15, 0.15) if randomize else v
                new_s = max(0.3, min(1.0, new_s))
                new_v = max(0.4, min(1.0, new_v))
                colors.append(self._hsv_to_hex(new_h, new_s, new_v))
        
        elif scheme == "split_complementary":
            for i, offset in enumerate(SPLIT_COMPLEMENTARY_OFFSETS * ((count // 3) + 1)):
                if len(colors) >= count:
                    break
                if randomize:
                    offset += random.uniform(-10, 10)
                new_h = (h + offset / 360) % 1.0
                variation = (i // 3) * 0.1
                new_s = s - variation + random.uniform(-0.1, 0.1) if randomize else s - variation
                new_v = v - variation * 0.5 + random.uniform(-0.1, 0.1) if randomize else v - variation * 0.5
                new_s = max(0.3, min(1.0, new_s))
                new_v = max(0.4, min(1.0, new_v))
                colors.append(self._hsv_to_hex(new_h, new_s, new_v))
        
        elif scheme == "triadic":
            for i in range(count):
                offset = (i % 3) * TRIADIC_SPREAD
                if randomize:
                    offset += random.uniform(-10, 10)
                new_h = (h + offset / 360) % 1.0
                variation = i // 3 * 0.15
                new_s = s - variation + random.uniform(-0.1, 0.1) if randomize else s - variation
                new_v = v - variation * 0.5 + random.uniform(-0.1, 0.1) if randomize else v - variation * 0.5
                new_s = max(0.3, min(1.0, new_s))
                new_v = max(0.4, min(1.0, new_v))
                colors.append(self._hsv_to_hex(new_h, new_s, new_v))
        
        elif scheme == "tetradic":
            for i in range(count):
                offset = TETRADIC_OFFSETS[i % 4]
                if randomize:
                    offset += random.uniform(-10, 10)
                new_h = (h + offset / 360) % 1.0
                variation = i // 4 * 0.1
                new_s = s - variation + random.uniform(-0.08, 0.08) if randomize else s - variation
                new_v = v - variation * 0.5 + random.uniform(-0.08, 0.08) if randomize else v - variation * 0.5
                new_s = max(0.3, min(1.0, new_s))
                new_v = max(0.4, min(1.0, new_v))
                colors.append(self._hsv_to_hex(new_h, new_s, new_v))
        
        elif scheme == "square":
            for i in range(count):
                offset = SQUARE_OFFSETS[i % 4]
                if randomize:
                    offset += random.uniform(-8, 8)
                new_h = (h + offset / 360) % 1.0
                variation = i // 4 * 0.1
                new_s = s - variation + random.uniform(-0.08, 0.08) if randomize else s - variation
                new_v = v - variation * 0.5 + random.uniform(-0.08, 0.08) if randomize else v - variation * 0.5
                new_s = max(0.3, min(1.0, new_s))
                new_v = max(0.4, min(1.0, new_v))
                colors.append(self._hsv_to_hex(new_h, new_s, new_v))
        
        else:  # random
            for _ in range(count):
                rand_h = random.random()
                rand_s = random.uniform(*saturation_range)
                rand_v = random.uniform(*value_range)
                colors.append(self._hsv_to_hex(rand_h, rand_s, rand_v))
        
        return colors[:count]
    
    def generate_theme_palette(
        self,
        scheme: PaletteScheme = "random",
        base_color: str = None,
        include_neutrals: bool = True,
        force_semantic_colors: bool = False
    ) -> Dict[str, str]:
        """Generate a complete theme palette with semantic colors.
        
        Args:
            scheme: Color harmony scheme
            base_color: Optional base color to build from
            include_neutrals: Add grayscale colors
            force_semantic_colors: Use standard green/yellow/red
            
        Returns:
            Dictionary mapping theme names to hex colors
        """
        colors = self.generate_palette(base_color, scheme, count=7)
        
        theme = {
            'primary': colors[0],
            'secondary': colors[1] if len(colors) > 1 else colors[0],
            'accent': colors[2] if len(colors) > 2 else colors[0],
        }
        
        if force_semantic_colors:
            theme['success'] = self._hsv_to_hex(0.33, 0.7, 0.8)
            theme['warning'] = self._hsv_to_hex(0.15, 0.8, 0.9)
            theme['error'] = self._hsv_to_hex(0.0, 0.8, 0.85)
            theme['info'] = colors[0]
        else:
            if len(colors) > 3:
                theme['success'] = colors[3]
                theme['warning'] = colors[4] if len(colors) > 4 else self._hsv_to_hex(0.15, 0.8, 0.9)
                theme['error'] = colors[5] if len(colors) > 5 else self._hsv_to_hex(0.0, 0.8, 0.85)
                theme['info'] = colors[6] if len(colors) > 6 else colors[0]
            else:
                theme['success'] = self._hsv_to_hex(0.33, 0.7, 0.8)
                theme['warning'] = self._hsv_to_hex(0.15, 0.8, 0.9)
                theme['error'] = self._hsv_to_hex(0.0, 0.8, 0.85)
                theme['info'] = colors[0]
        
        if include_neutrals:
            theme['background'] = '#1a1a1a'
            theme['foreground'] = '#e0e0e0'
            theme['muted'] = '#666666'
            theme['border'] = '#333333'
        
        return theme
    
    def generate_accessible_theme(
        self,
        base_color: str,
        scheme: PaletteScheme = "complementary",
        background: str = "#1a1a1a",
        min_contrast: float = 4.5,
        wcag_level: str = "AA"
    ) -> Dict[str, str]:
        """Generate theme palette with WCAG contrast validation.
        
        Args:
            base_color: Base color to build theme from
            scheme: Color harmony scheme
            background: Background color to test contrast against
            min_contrast: Minimum contrast ratio
            wcag_level: WCAG level "AA" or "AAA"
            
        Returns:
            Dictionary with accessible color theme
        """
        theme = self.generate_theme_palette(scheme, base_color, force_semantic_colors=True)
        
        for key in ['primary', 'secondary', 'accent', 'error', 'warning', 'success', 'info']:
            if key in theme:
                original = theme[key]
                adjusted = self.ensure_contrast(original, background, min_contrast)
                theme[key] = adjusted
        
        theme['background'] = background
        theme['foreground'] = self.ensure_contrast('#e0e0e0', background, min_contrast)
        
        return theme
    
    def preview_palette(self, colors: List[str], width: int = 40, show_info: bool = True) -> str:
        """Generate a text preview of a color palette.
        
        Args:
            colors: List of hex colors
            width: Width of each color block
            show_info: Show additional color information
            
        Returns:
            Formatted string showing colored blocks
        """
        output = []
        for i, color in enumerate(colors):
            block = "█" * width
            styled_block = self.style(block, color=color)
            line = f"{i+1}. {color:8s} {styled_block}"
            
            if show_info:
                h, s, v = self._hex_to_hsv(color)
                line += f"  H:{h*360:3.0f}° S:{s*100:3.0f}% V:{v*100:3.0f}%"
            
            output.append(line)
        return "\n".join(output)
    
    def apply_palette_theme(self, palette: Dict[str, str], register_styles: bool = True):
        """Apply a generated palette as the active theme.
        
        Args:
            palette: Dictionary from generate_theme_palette()
            register_styles: Register each color as a custom style
        """
        theme_styles = {}
        for name, color in palette.items():
            theme_styles[name] = {"color": color, "bg": None, "look": None}
        
        self._current_theme = theme_styles
        
        if register_styles:
            for name, style_def in theme_styles.items():
                self.create(name, **style_def)
    
    # ============================================
    # Persistence Methods
    # ============================================
    
    @staticmethod
    def save_palette(colors: List[str], filename: str, metadata: Optional[Dict] = None):
        """Save color palette to JSON file.
        
        Args:
            colors: List of hex colors to save
            filename: Output file path
            metadata: Optional metadata
        """
        data = {
            "colors": colors,
            "metadata": metadata or {}
        }
        
        filepath = Path(filename)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    @staticmethod
    def load_palette(filename: str) -> Tuple[List[str], Dict]:
        """Load color palette from JSON file.
        
        Args:
            filename: Input file path
            
        Returns:
            Tuple of (colors list, metadata dict)
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        return data.get("colors", []), data.get("metadata", {})
    
    @staticmethod
    def save_theme(theme: Dict[str, str], filename: str, metadata: Optional[Dict] = None):
        """Save theme palette to JSON file.
        
        Args:
            theme: Theme dictionary
            filename: Output file path
            metadata: Optional metadata
        """
        data = {
            "theme": theme,
            "metadata": metadata or {}
        }
        
        filepath = Path(filename)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    @staticmethod
    def load_theme(filename: str) -> Tuple[Dict[str, str], Dict]:
        """Load theme palette from JSON file.
        
        Args:
            filename: Input file path
            
        Returns:
            Tuple of (theme dict, metadata dict)
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        return data.get("theme", {}), data.get("metadata", {})
    
    # ============================================
    # Factory Methods for Inner Classes
    # ============================================
    
    def Table(
        self,
        title: str = None,
        caption: str = None,
        style: str = None,
        title_style: str = None,
        caption_style: str = None,
        header_style: str = "bold",
        border_style: str = None,
        show_header: bool = True,
        show_lines: bool = False,
        padding: Tuple[int, int] = (0, 1),
        expand: bool = False,
        min_width: int = None,
        box: str = "rounded"
    ) -> '_Table':
        """Create a rich-style table with customizable styling and borders.
        
        Example:
            >>> vg = Vargula()
            >>> table = vg.Table(title="Users", style="cyan")
            >>> table.add_column("Name", style="bold")
            >>> table.add_column("Email", style="blue")
            >>> table.add_row("Alice", "alice@example.com")
            >>> print(table)
        """
        return self._Table(
            vargula=self,
            title=title,
            caption=caption,
            style=style,
            title_style=title_style,
            caption_style=caption_style,
            header_style=header_style,
            border_style=border_style,
            show_header=show_header,
            show_lines=show_lines,
            padding=padding,
            expand=expand,
            min_width=min_width,
            box=box
        )
    
    def ProgressBar(
        self,
        total: int = 100,
        desc: str = "",
        unit: str = "it",
        bar_width: int = 40,
        complete_style: str = "green",
        incomplete_style: str = "bright_black",
        percentage_style: str = "cyan",
        desc_style: str = "bold",
        show_percentage: bool = True,
        show_count: bool = True,
        show_rate: bool = True,
        show_eta: bool = True,
        bar_format: str = None,
        refresh_rate: float = 0.1
    ) -> '_ProgressBar':
        """Create a rich-style progress bar with customizable appearance.
        
        Example:
            >>> vg = Vargula()
            >>> with vg.ProgressBar(total=100, desc="Processing") as pbar:
            ...     for i in range(100):
            ...         pbar.update(1)
            ...         time.sleep(0.01)
        """
        return self._ProgressBar(
            vargula=self,
            total=total,
            desc=desc,
            unit=unit,
            bar_width=bar_width,
            complete_style=complete_style,
            incomplete_style=incomplete_style,
            percentage_style=percentage_style,
            desc_style=desc_style,
            show_percentage=show_percentage,
            show_count=show_count,
            show_rate=show_rate,
            show_eta=show_eta,
            bar_format=bar_format,
            refresh_rate=refresh_rate
        )
    
    def MultiProgress(self) -> '_MultiProgress':
        """Create a manager for multiple progress bars simultaneously.
        
        Example:
            >>> vg = Vargula()
            >>> with vg.MultiProgress() as mp:
            ...     task1 = mp.add_task("Task 1", total=100)
            ...     task2 = mp.add_task("Task 2", total=50)
            ...     for i in range(100):
            ...         mp.update(task1, 1)
            ...         if i % 2 == 0:
            ...             mp.update(task2, 1)
        """
        return self._MultiProgress(vargula=self)
    
    # ============================================
    # _Table Class (Inner - Private)
    # ============================================
    
    class _Table:
        """Rich-style table with customizable styling and borders.
        
        Access via vg.Table() factory method.
        """
        
        def __init__(
            self,
            vargula: 'Vargula',
            title: str = None,
            caption: str = None,
            style: str = None,
            title_style: str = None,
            caption_style: str = None,
            header_style: str = "bold",
            border_style: str = None,
            show_header: bool = True,
            show_lines: bool = False,
            padding: Tuple[int, int] = (0, 1),
            expand: bool = False,
            min_width: int = None,
            box: str = "rounded"
        ):
            """Initialize a table."""
            self.vg = vargula
            self.title = title
            self.caption = caption
            self.style = style
            self.title_style = title_style or "bold"
            self.caption_style = caption_style or "dim"
            self.header_style = header_style
            self.border_style = border_style
            self.show_header = show_header
            self.show_lines = show_lines
            self.padding = padding
            self.expand = expand
            self.min_width = min_width
            self.box = box
            
            self.columns = []
            self.rows = []
            
            self._box_chars = self._get_box_chars(box)
        
        def _get_box_chars(self, box_type: str) -> Dict[str, str]:
            """Get box drawing characters for border style."""
            boxes = {
                "rounded": {
                    "tl": "╭", "tr": "╮", "bl": "╰", "br": "╯",
                    "h": "─", "v": "│", "lt": "├", "rt": "┤",
                    "tt": "┬", "bt": "┴", "cross": "┼"
                },
                "square": {
                    "tl": "┌", "tr": "┐", "bl": "└", "br": "┘",
                    "h": "─", "v": "│", "lt": "├", "rt": "┤",
                    "tt": "┬", "bt": "┴", "cross": "┼"
                },
                "double": {
                    "tl": "╔", "tr": "╗", "bl": "╚", "br": "╝",
                    "h": "═", "v": "║", "lt": "╠", "rt": "╣",
                    "tt": "╦", "bt": "╩", "cross": "╬"
                },
                "heavy": {
                    "tl": "┏", "tr": "┓", "bl": "┗", "br": "┛",
                    "h": "━", "v": "┃", "lt": "┣", "rt": "┫",
                    "tt": "┳", "bt": "┻", "cross": "╋"
                },
                "minimal": {
                    "tl": " ", "tr": " ", "bl": " ", "br": " ",
                    "h": "─", "v": " ", "lt": " ", "rt": " ",
                    "tt": " ", "bt": " ", "cross": " "
                },
                "none": {
                    "tl": " ", "tr": " ", "bl": " ", "br": " ",
                    "h": " ", "v": " ", "lt": " ", "rt": " ",
                    "tt": " ", "bt": " ", "cross": " "
                }
            }
            return boxes.get(box_type, boxes["rounded"])
        
        def add_column(
            self,
            header: str,
            style: str = None,
            justify: str = "left",
            no_wrap: bool = False,
            overflow: str = "ellipsis",
            width: int = None,
            min_width: int = None,
            max_width: int = None
        ):
            """Add a column to the table."""
            header_length = Vargula.length(header)
            
            self.columns.append({
                "header": header,
                "style": style,
                "justify": justify,
                "no_wrap": no_wrap,
                "overflow": overflow,
                "width": width,
                "min_width": min_width or header_length,
                "max_width": max_width,
                "actual_width": width or header_length
            })
            
            for row in self.rows:
                row["cells"].append("")
        
        def add_row(self, *cells, style: str = None):
            """Add a row of data to the table."""
            cells_list = list(cells)
            if len(cells_list) < len(self.columns):
                cells_list.extend([""] * (len(self.columns) - len(cells_list)))
            elif len(cells_list) > len(self.columns):
                raise ValueError(f"Too many cells: expected {len(self.columns)}, got {len(cells_list)}")
            
            self.rows.append({"cells": cells_list, "style": style})
        
        def update_cell(self, row_idx: int, col_idx: int, value: str):
            """Update a specific cell value."""
            if 0 <= row_idx < len(self.rows) and 0 <= col_idx < len(self.columns):
                self.rows[row_idx]["cells"][col_idx] = value
            else:
                raise IndexError(f"Cell position ({row_idx}, {col_idx}) out of bounds")
        
        def _calculate_widths(self, terminal_width: int = 80):
            """Calculate optimal column widths."""
            if not self.columns:
                return
            
            if self.expand:
                available = terminal_width - len(self.columns) - 1
            else:
                available = terminal_width
            
            for col_idx, col in enumerate(self.columns):
                if col["width"]:
                    col["actual_width"] = col["width"]
                else:
                    max_content = col["min_width"]
                    
                    if self.rows:
                        for row in self.rows:
                            if col_idx < len(row["cells"]):
                                cell_text = str(row["cells"][col_idx])
                                cell_length = Vargula.length(cell_text)
                                max_content = max(max_content, cell_length)
                    
                    if col["max_width"]:
                        max_content = min(max_content, col["max_width"])
                    
                    col["actual_width"] = max_content
            
            total = sum(c["actual_width"] for c in self.columns)
            if self.min_width and total < self.min_width:
                extra = self.min_width - total
                per_col = extra // len(self.columns)
                for col in self.columns:
                    col["actual_width"] += per_col
        
        def _justify_text(self, text: str, width: int, align: str) -> str:
            """Justify text within given width."""
            text_len = Vargula.length(text)
            if text_len >= width:
                return text[:width]
            
            padding = width - text_len
            if align == "center":
                left = padding // 2
                right = padding - left
                return " " * left + text + " " * right
            elif align == "right":
                return " " * padding + text
            else:
                return text + " " * padding
        
        def _apply_style(self, text: str, style_str: str) -> str:
            """Apply a style string to text."""
            if not style_str:
                return text
            
            styles = style_str.strip().split()
            result = text
            for s in reversed(styles):
                result = f"<{s}>{result}</{s}>"
            
            return self.vg.format(result)
        
        def _render_border(self, left: str, mid: str, right: str, junction: str) -> str:
            """Render a horizontal border line."""
            parts = [left]
            pad_h = self.padding[1]
            
            for i, col in enumerate(self.columns):
                parts.append(mid * (col["actual_width"] + pad_h * 2))
                if i < len(self.columns) - 1:
                    parts.append(junction)
            parts.append(right)
            
            line = "".join(parts)
            if self.border_style:
                return self._apply_style(line, self.border_style)
            return line
        
        def _render_row(self, cells: List[str], cell_styles: List[str] = None, row_style: str = None) -> str:
            """Render a single row."""
            parts = []
            v_char = self._box_chars["v"]
            if self.border_style:
                v_char = self._apply_style(v_char, self.border_style)
            
            parts.append(v_char)
            
            pad_v, pad_h = self.padding
            
            for i, (cell, col) in enumerate(zip(cells, self.columns)):
                cell_text = str(cell)
                
                cell_length = Vargula.length(cell_text)
                if cell_length > col["actual_width"]:
                    if col["overflow"] == "ellipsis":
                        if col["actual_width"] > 0:
                            cell_text = cell_text[:col["actual_width"]-1] + "…"
                        else:
                            cell_text = ""
                    else:
                        cell_text = cell_text[:col["actual_width"]]
                
                justified = self._justify_text(cell_text, col["actual_width"], col["justify"])
                
                styled = justified
                if cell_styles and i < len(cell_styles) and cell_styles[i]:
                    styled = self._apply_style(justified, cell_styles[i])
                elif col["style"]:
                    styled = self._apply_style(justified, col["style"])
                elif row_style:
                    styled = self._apply_style(justified, row_style)
                elif self.style:
                    styled = self._apply_style(justified, self.style)
                
                parts.append(" " * pad_h + styled + " " * pad_h)
                parts.append(v_char)
            
            return "".join(parts)
        
        def __str__(self) -> str:
            """Render the table as a string."""
            if not self.columns:
                return ""
            
            self._calculate_widths()
            lines = []
            
            if self.title:
                title_text = self.title
                if self.title_style:
                    title_text = self._apply_style(title_text, self.title_style)
                lines.append(title_text)
            
            lines.append(self._render_border(
                self._box_chars["tl"],
                self._box_chars["h"],
                self._box_chars["tr"],
                self._box_chars["tt"]
            ))
            
            if self.show_header:
                headers = [col["header"] for col in self.columns]
                header_styles = [self.header_style] * len(self.columns)
                lines.append(self._render_row(headers, header_styles))
                
                lines.append(self._render_border(
                    self._box_chars["lt"],
                    self._box_chars["h"],
                    self._box_chars["rt"],
                    self._box_chars["cross"]
                ))
            
            for idx, row in enumerate(self.rows):
                lines.append(self._render_row(row["cells"], row_style=row["style"]))
                
                if self.show_lines and idx < len(self.rows) - 1:
                    lines.append(self._render_border(
                        self._box_chars["lt"],
                        self._box_chars["h"],
                        self._box_chars["rt"],
                        self._box_chars["cross"]
                    ))
            
            lines.append(self._render_border(
                self._box_chars["bl"],
                self._box_chars["h"],
                self._box_chars["br"],
                self._box_chars["bt"]
            ))
            
            if self.caption:
                caption_text = self.caption
                if self.caption_style:
                    caption_text = self._apply_style(caption_text, self.caption_style)
                lines.append(caption_text)
            
            return "\n".join(lines)
    
    # ============================================
    # _ProgressBar Class (Inner - Private)
    # ============================================
    
    class _ProgressBar:
        """Rich-style progress bar with customizable appearance.
        
        Access via vg.ProgressBar() factory method.
        """
        
        def __init__(
            self,
            vargula: 'Vargula',
            total: int = 100,
            desc: str = "",
            unit: str = "it",
            bar_width: int = 40,
            complete_style: str = "green",
            incomplete_style: str = "bright_black",
            percentage_style: str = "cyan",
            desc_style: str = "bold",
            show_percentage: bool = True,
            show_count: bool = True,
            show_rate: bool = True,
            show_eta: bool = True,
            bar_format: str = None,
            refresh_rate: float = 0.1
        ):
            """Initialize a progress bar."""
            self.vg = vargula
            self.total = total
            self.desc = desc
            self.unit = unit
            self.bar_width = bar_width
            self.complete_style = complete_style
            self.incomplete_style = incomplete_style
            self.percentage_style = percentage_style
            self.desc_style = desc_style
            self.show_percentage = show_percentage
            self.show_count = show_count
            self.show_rate = show_rate
            self.show_eta = show_eta
            self.bar_format = bar_format
            self.refresh_rate = refresh_rate
            
            self.current = 0
            self.start_time = None
            self.last_update_time = 0
            self._finished = False
        
        def _format_time(self, seconds: float) -> str:
            """Format seconds as HH:MM:SS or MM:SS."""
            if seconds < 0:
                return "--:--"
            
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            secs = int(seconds % 60)
            
            if hours > 0:
                return f"{hours:02d}:{minutes:02d}:{secs:02d}"
            return f"{minutes:02d}:{secs:02d}"
        
        def _render_bar(self) -> str:
            """Render the progress bar."""
            if self.total == 0:
                percent = 0
            else:
                percent = self.current / self.total
            
            filled = int(self.bar_width * percent)
            empty = self.bar_width - filled
            
            bar_complete = "█" * filled
            bar_incomplete = "░" * empty
            
            if self.complete_style:
                bar_complete = self._apply_style(bar_complete, self.complete_style)
            if self.incomplete_style:
                bar_incomplete = self._apply_style(bar_incomplete, self.incomplete_style)
            
            return bar_complete + bar_incomplete
        
        def _apply_style(self, text: str, style_str: str) -> str:
            """Apply a style string to text."""
            if not style_str:
                return text
            
            styles = style_str.strip().split()
            result = text
            for s in reversed(styles):
                result = f"<{s}>{result}</{s}>"
            
            return self.vg.format(result)
        
        def _render(self) -> str:
            """Render the complete progress line."""
            parts = []
            
            if self.desc:
                desc_text = self.desc
                if self.desc_style:
                    desc_text = self._apply_style(desc_text, self.desc_style)
                parts.append(desc_text)
            
            parts.append(self._render_bar())
            
            if self.show_percentage:
                percent = (self.current / self.total * 100) if self.total > 0 else 0
                pct_text = f"{percent:>5.1f}%"
                if self.percentage_style:
                    pct_text = self._apply_style(pct_text, self.percentage_style)
                parts.append(pct_text)
            
            if self.show_count:
                parts.append(f"{self.current}/{self.total} {self.unit}")
            
            if self.show_rate and self.start_time:
                elapsed = time.time() - self.start_time
                if elapsed > 0:
                    rate = self.current / elapsed
                    parts.append(f"[{rate:.2f} {self.unit}/s]")
            
            if self.show_eta and self.start_time and self.current > 0:
                elapsed = time.time() - self.start_time
                rate = self.current / elapsed if elapsed > 0 else 0
                if rate > 0:
                    remaining = (self.total - self.current) / rate
                    parts.append(f"ETA: {self._format_time(remaining)}")
            
            return " ".join(parts)
        
        def update(self, n: int = 1):
            """Update progress by n steps."""
            if self.start_time is None:
                self.start_time = time.time()
            
            self.current = min(self.current + n, self.total)
            
            current_time = time.time()
            if current_time - self.last_update_time >= self.refresh_rate or self.current == self.total:
                self._display()
                self.last_update_time = current_time
        
        def _display(self):
            """Display the progress bar."""
            if not self.vg.is_enabled():
                return
            
            line = self._render()
            print(f"\r{line}", end="", flush=True)
            
            if self.current >= self.total and not self._finished:
                print()
                self._finished = True
        
        def close(self):
            """Finish the progress bar."""
            if not self._finished:
                self.current = self.total
                self._display()
        
        def __enter__(self):
            """Context manager entry."""
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            """Context manager exit."""
            self.close()
    
    # ============================================
    # _MultiProgress Class (Inner - Private)
    # ============================================
    
    class _MultiProgress:
        """Manage multiple progress bars simultaneously.
        
        Access via vg.MultiProgress() factory method.
        """
        
        def __init__(self, vargula: 'Vargula'):
            """Initialize multi-progress manager."""
            self.vg = vargula
            self.tasks = {}
            self.task_counter = 0
        
        def add_task(self, desc: str, total: int = 100, **kwargs) -> int:
            """Add a new progress task.
            
            Args:
                desc: Task description
                total: Total iterations
                **kwargs: Additional ProgressBar arguments
                
            Returns:
                Task ID for updating
            """
            task_id = self.task_counter
            self.task_counter += 1
            
            self.tasks[task_id] = {
                "progress": self.vg.ProgressBar(total=total, desc=desc, **kwargs),
                "visible": True
            }
            
            return task_id
        
        def update(self, task_id: int, n: int = 1):
            """Update a specific task."""
            if task_id in self.tasks:
                self.tasks[task_id]["progress"].update(n)
        
        def remove_task(self, task_id: int):
            """Remove a task from display."""
            if task_id in self.tasks:
                self.tasks[task_id]["visible"] = False
        
        def __enter__(self):
            """Context manager entry."""
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            """Context manager exit."""
            for task in self.tasks.values():
                task["progress"].close()


# ============================================
# Module-level exports
# ============================================

__all__ = [
    # Main class
    "Vargula",
    
    # Type definitions
    "PaletteScheme",
    "ColorBlindType",
    
    # Constants
    "COLORS",
    "BG_COLORS",
    "LOOKS",
    
    # Helper function
    "progress_bar",
]