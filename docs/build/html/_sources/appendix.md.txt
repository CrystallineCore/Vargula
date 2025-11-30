# Appendix

## Quick Reference

### Color Name Cheat Sheet

**Basic Colors:**
```
black    red      green    yellow
blue     magenta  cyan     white
```

**Bright Colors:**
```
bright_black    bright_red      bright_green    bright_yellow
bright_blue     bright_magenta  bright_cyan     bright_white
```

### Text Decoration Cheat Sheet

```
bold          dim           italic        underline
blink         reverse       hidden        strikethrough
```

### Box Style Cheat Sheet

```
rounded    ╭───╮
           │   │
           ╰───╯

square     ┌───┐
           │   │
           └───┘

double     ╔═══╗
           ║   ║
           ╚═══╝

heavy      ┏━━━┓
           ┃   ┃
           ┗━━━┛

minimal    ┌───┐
               
           └───┘

none       (no borders)
```

### Color Harmony Schemes

```
monochromatic         - Single hue with variations
analogous             - Adjacent colors (±30°)
complementary         - Opposite colors (180°)
triadic               - Three evenly spaced (120°)
tetradic              - Four colors (60°, 180°, 240°)
split_complementary   - Base + two adjacent to complement
square                - Four evenly spaced (90°)
random                - Random selection
```

---

## Color Theory Guide

### Understanding Color Spaces

**RGB (Red, Green, Blue)**
- Additive color model used by screens
- Values: 0-255 for each channel
- Example: `(255, 0, 0)` is pure red

**Hex Colors**
- Hexadecimal representation of RGB
- Format: `#RRGGBB`
- Example: `#FF0000` is pure red

**HSV (Hue, Saturation, Value)**
- Hue: Color type (0-360°)
- Saturation: Color intensity (0-1)
- Value: Brightness (0-1)
- More intuitive for color manipulation

### Color Wheel Relationships

```
          Yellow
            │
    Yellow-│-Orange
   Green   │   Orange
      │    │    │
Green ─────┼───── Red
      │    │    │
   Cyan    │  Magenta
     Blue-─┼─Magenta
          Blue
```

**Complementary Colors:**
- Red ↔ Cyan
- Green ↔ Magenta
- Blue ↔ Yellow

**Analogous Colors:**
- Red, Orange, Yellow
- Blue, Cyan, Green
- Magenta, Red, Orange

### Practical Color Selection

**For Backgrounds:**
```python
# Dark themes
background = "#1a1a1a"  # Very dark gray
background = "#0d1117"  # GitHub dark
background = "#282c34"  # VS Code dark

# Light themes
background = "#ffffff"  # Pure white
background = "#f6f8fa"  # GitHub light
background = "#fafafa"  # Material light
```

**For Text:**
```python
# High contrast
fg = "#ffffff"  # White on dark
fg = "#000000"  # Black on light

# Reduced contrast (softer)
fg = "#e0e0e0"  # Light gray on dark
fg = "#24292f"  # Dark gray on light
```

**For Semantic Colors:**
```python
success = "#2ecc71"  # Green
warning = "#f39c12"  # Orange
error = "#e74c3c"    # Red
info = "#3498db"     # Blue
```

---

## WCAG Compliance Guide

### Contrast Ratio Requirements

**Level AA (Minimum):**
- Normal text (< 18pt): 4.5:1
- Large text (≥ 18pt or ≥ 14pt bold): 3:1

**Level AAA (Enhanced):**
- Normal text: 7:1
- Large text: 4.5:1

### Testing Color Combinations

```python
import vargula

vg = vargula.Vargula()

# Test a color combination
fg = "#3498db"
bg = "#ffffff"

ratio = vg.calculate_contrast_ratio(fg, bg)
print(f"Contrast ratio: {ratio:.2f}:1")

# Check WCAG compliance
if vg.meets_wcag(fg, bg, "AA"):
    print("✓ Meets WCAG AA")
else:
    print("✗ Does not meet WCAG AA")
```

### Automatic Compliance

```python
# Automatically adjust color to meet requirements
fg = "#888888"
bg = "#999999"

# Ensure at least 4.5:1 contrast
accessible_fg = vg.ensure_contrast(fg, bg, min_ratio=4.5)
print(f"Original: {fg}")
print(f"Adjusted: {accessible_fg}")
```

### Color Blindness Considerations

**Common Types:**
- **Deuteranopia** (green-blind): 5% of males
- **Protanopia** (red-blind): 1% of males
- **Tritanopia** (blue-blind): < 0.1% of population

**Testing Your Palette:**
```python
colors = ["#FF0000", "#00FF00", "#0000FF"]

# Test for deuteranopia (most common)
is_safe, problems = vg.validate_colorblind_safety(colors, "deuteranopia")

if not is_safe:
    print("⚠ Palette has distinguishability issues:")
    for i, j in problems:
        print(f"  Colors {i} and {j} are too similar")
```

**Best Practices:**
- Don't rely on color alone for information
- Use patterns, icons, or labels alongside colors
- Test with simulation tools
- Use sufficient contrast between adjacent colors

---

## Performance Tips

### Minimize Redundant Formatting

**Bad:**
```python
# Formats the same style repeatedly
for i in range(1000):
    print(vg.format(f"<bold><red>Item {i}</red></bold>"))
```

**Good:**
```python
# Create style once, reuse
vg.create("item", color="red", look="bold")
for i in range(1000):
    print(vg.format(f"<item>Item {i}</item>"))
```

### Batch Operations

**Bad:**
```python
# Many small writes
for line in data:
    print(vg.format(f"<cyan>{line}</cyan>"))
```

**Good:**
```python
# Single formatted output
output = "\n".join(vg.format(f"<cyan>{line}</cyan>") for line in data)
print(output)
```

### Disable Styling When Not Needed

```python
from vargula import Vargula
import sys

vg = Vargula()

# Disable for non-TTY output (pipes, files)
if not sys.stdout.isatty():
    vg.disable()

# Your code runs normally
print(vg.style("Text", color="red"))  # Plain text if disabled
```

### Efficient Progress Bars

```python
from vargula import Vargula

vg = Vargula()

# Set appropriate refresh rate
pbar = vg.ProgressBar(
    total=10000,
    refresh_rate=0.5  # Update at most every 0.5 seconds
)

for i in range(10000):
    # Fast operations
    pbar.update(1)
```

---

## Troubleshooting

### Colors Not Displaying

**Problem:** Colors appear as plain text or garbage characters.

**Solutions:**
1. **Check terminal support:**
   ```python
   import sys
   print(f"Terminal: {sys.stdout.isatty()}")
   print(f"Term type: {os.environ.get('TERM', 'unknown')}")
   ```

2. **Enable ANSI on Windows:**
   ```python
   import os
   os.system('')  # Enables ANSI support on Windows 10+
   ```

3. **Force enable in IDE:**
   ```python
   from vargula import Vargula
   vg = Vargula()
   vg.enable()  # Force styling even if auto-detection fails
   ```

### Layout Issues with Tables

**Problem:** Table doesn't fit terminal width.

**Solutions:**
```python
# Get terminal width
import shutil
width, height = shutil.get_terminal_size()

# Create table with appropriate width
table = vg.Table(max_width=width - 4)

# Or expand to fill width
table = vg.Table(expand=True)
```

### Progress Bar Flickering

**Problem:** Progress bar updates too frequently.

**Solution:**
```python
# Increase refresh rate
pbar = vg.ProgressBar(refresh_rate=0.2)  # Max 5 updates/second

# Or update in larger chunks
for i in range(0, total, 10):
    # Do work...
    pbar.update(10)
```

### Memory Issues with Large Outputs

**Problem:** Styling large amounts of text causes memory issues.

**Solution:**
```python
# Stream output instead of building strings
with open("output.txt", "w") as f:
    for item in large_dataset:
        formatted = vg.format(f"<cyan>{item}</cyan>")
        f.write(formatted + "\n")
        # Don't accumulate in memory
```

### Style Conflicts

**Problem:** Nested styles don't work as expected.

**Solution:**
```python
# Be explicit about style boundaries
vg.create("outer", color="red")
vg.create("inner", color="blue")

# This works
print(vg.format("<outer>Red <inner>Blue</inner> Red again</outer>"))

# Not this (ambiguous nesting)
# print(vg.format("<red>Red <blue>Blue</red> What color?</blue>"))
```

---

## Migration Guide

### From Print Statements

**Before:**
```python
print("Error: Connection failed")
print("Success: File saved")
```

**After:**
```python
vg = Vargula()
vg.write("<error>Error:</error> Connection failed")
vg.write("<success>Success:</success> File saved")
```

### From Manual ANSI Codes

**Before:**
```python
RED = "\033[31m"
RESET = "\033[0m"
print(f"{RED}Error{RESET}")
```

**After:**
```python
from vargula import Vargula
vg = Vargula()
print(vg.style("Error", color="red"))
# Or
print(vg.format("<red>Error</red>"))
```

### From Other Styling Libraries

**From `colorama`:**
```python
# Before (colorama)
from colorama import Fore, Style
print(Fore.RED + "Error" + Style.RESET_ALL)

# After (vargula)
from vargula import Vargula
vg = Vargula()
print(vg.style("Error", color="red"))
```

**From `termcolor`:**
```python
# Before (termcolor)
from termcolor import colored
print(colored("Error", "red", attrs=["bold"]))

# After (vargula)
from vargula import Vargula
vg = Vargula()
print(vg.style("Error", color="red", look="bold"))
```

**From `rich`:**
```python
# Before (rich)
from rich import print as rprint
rprint("[red bold]Error[/red bold]")

# After (vargula)
from vargula import Vargula
vg = Vargula()
vg.write("<red><bold>Error</bold></red>")
```

### Best Practices for Migration

1. **Start with custom styles:**
   ```python
   # Define your styles upfront
   vg.create("error", color="red", look="bold")
   vg.create("success", color="green", look="bold")
   vg.create("info", color="cyan")
   ```

2. **Use themes for consistency:**
   ```python
   # Create a theme matching your brand
   theme = {
       "primary": "#yourcolor",
       "error": "#yourcolor",
       # ...
   }
   vg.set_theme(theme)
   ```

3. **Gradual replacement:**
   - Replace print statements incrementally
   - Test each section before moving on
   - Keep old code commented until verified

4. **Create helper functions:**
   ```python
   def error(msg):
       vg.write(f"<error>✗ {msg}</error>")
   
   def success(msg):
       vg.write(f"<success>✓ {msg}</success>")
   
   def info(msg):
       vg.write(f"<info>ℹ {msg}</info>")
   ```

---

## Additional Resources

### Example Projects

- **CLI Dashboard:** Full-featured terminal dashboard with tables and progress bars
- **Log Analyzer:** Colorized log file viewer with syntax highlighting
- **Terminal Game:** Roguelike game using Vargula for graphics
- **API Monitor:** Real-time API status display with color-coded responses

### Color Palette Generators

```python
# Generate and preview palettes
from vargula import Vargula

vg = Vargula()
# Try different schemes
schemes = ["analogous", "complementary", "triadic", "tetradic"]
base = "#3498db"

for scheme in schemes:
    colors = vg.generate_palette(base, scheme, count=5)
    print(f"\n{scheme.title()} Palette:")
    print(vg.preview_palette(colors))
```

### Community Themes

Share and load community-created themes:

```python
# Save your theme
theme = vg.generate_theme_palette("complementary", "#e74c3c")
vg.save_theme(theme, "my_awesome_theme.json", metadata={
    "name": "Sunset",
    "author": "YourName",
    "description": "Warm, vibrant sunset colors"
})

# Load and use community themes
theme, meta = vg.load_theme("community_theme.json")
print(f"Loading {meta['name']} by {meta['author']}")
vg.apply_palette_theme(theme)
```

---

## Version Compatibility

**Python Requirements:**
- Minimum: Python 3.7
- Recommended: Python 3.9+

**Terminal Compatibility:**
- ✓ Modern terminals (ANSI support)
- ✓ Windows 10+ (with ANSI enabled)
- ✓ macOS Terminal
- ✓ Linux terminals (xterm, gnome-terminal, etc.)
- ✓ VS Code integrated terminal
- ✓ PyCharm terminal
- ⚠ Windows Command Prompt (limited support)
- ✗ Very old terminals without ANSI support

---

**Last Updated:** 2025-11-30  
**Library Version:** 2.0.0