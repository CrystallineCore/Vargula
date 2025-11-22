# Changelog

All notable changes to the vargula project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - 2024-11-22

### Added
- **Background color tag syntax**: New `<@color>` tag convention for inline background styling
  - Hex background colors: `<@#FF0000>text</@#FF0000>`, `<@#F00>text</@#F00>`
  - Named background colors: `<@red>text</@red>`, `<@yellow>text</@yellow>`
  - Full symmetry with foreground color tags
  - `@` prefix is used for setting background-colors

### Enhanced
- **`format()` function**: Enhanced tag parsing to support background color syntax
  - Proper validation of hex color codes (3 or 6 characters)
  - Maintains full backward compatibility with existing tags

### Tag Syntax Summary
- `<#hexcode>` - Foreground hex color (required `#` prefix)
- `<@#hexcode>` - Background hex color 
- `<colorname>` - Named foreground color
- `<@colorname>` - Named background color (new!)
- `<lookname>` - Text style (bold, italic, etc.)

### Examples
```python
import vargula as vg

# Named background colors
vg.write("<@yellow>Yellow background</@yellow>")
vg.write("<@red>Red background</@red>")

# Hex background colors
vg.write("<@#FF0000>Hex red background</@#FF0000>")
vg.write("<@#F00>Short hex red</@#F00>")

# Combining foreground and background
vg.write("<#FFFFFF><@#000000>White on black</@#000000></#FFFFFF>")
vg.write("<green><@black>Green on black</@black></green>")

# Complex nesting
vg.write("<@yellow>Yellow <@#FF0000>then red</@#FF0000> back to yellow</@yellow>")
```

## [1.0.3] - 2024-11-22

### Added
- **Enhanced `write()` function**: Now works exactly like built-in `print()`
  - Accepts multiple positional arguments
  - Supports `sep` parameter for custom separators
  - Supports `end` parameter for custom line endings
  - Supports `file` parameter for output redirection
  - Supports `flush` parameter for stream control
  - Automatically formats all arguments with markup tags

### Changed
- `write()` signature changed from `write(text)` to `write(*args, sep=" ", end="\n", file=None, flush=False)`

### Examples
```python
# New capabilities
vg.write("Hello", "<red>World</red>", sep=" → ")
vg.write("user", "localhost", sep=vg.format("<cyan>@</cyan>"))
vg.write("<bold>Processing</bold>", end="... ")
```

## [1.0.2] - 2024-11-20

### Added
- Advanced color palette generation system
  - `generate_palette()`: Create palettes using color theory schemes
  - `generate_theme_palette()`: Generate complete semantic theme palettes
  - `generate_accessible_theme()`: WCAG-compliant theme generation
  - Support for 8 color harmony schemes: monochromatic, analogous, complementary, triadic, tetradic, split_complementary, square, random

- Color manipulation functions
  - `lighten()`, `darken()`: Adjust brightness
  - `saturate()`, `desaturate()`: Adjust saturation
  - `shift_hue()`: Rotate hue by degrees
  - `invert()`: Invert colors
  - `mix()`: Blend two colors together

- Accessibility features
  - `calculate_contrast_ratio()`: WCAG 2.1 contrast calculation
  - `meets_wcag()`: Check WCAG AA/AAA compliance
  - `ensure_contrast()`: Auto-adjust colors for minimum contrast
  - `simulate_colorblindness()`: Preview colors for colorblind users (6 types)
  - `validate_colorblind_safety()`: Check palette distinguishability

- Palette utilities
  - `preview_palette()`: Visual palette preview in terminal
  - `apply_palette_theme()`: Apply generated themes
  - `save_palette()`, `load_palette()`: Persist palettes to JSON
  - `save_theme()`, `load_theme()`: Persist themes to JSON

- Rich UI components
  - `Table`: Fully-featured table with customizable styling
    - Multiple box styles (rounded, square, double, heavy, minimal, none)
    - Column alignment and styling
    - Row styling and cell updates
    - Title, caption, and border customization
  - `ProgressBar`: Animated progress indicators
    - Customizable appearance and metrics
    - ETA, rate, and percentage display
  - `MultiProgress`: Manage multiple progress bars
  - `progress_bar()`: Wrapper for iterables

### Fixed
- Table rendering with proper column width calculations
- Table cell handling when columns are added after rows exist
- Better ellipsis handling in table overflow
- Improved nested tag processing in `format()`

## [1.0.1] - 2024-11-15

### Added
- Core styling functions
  - `style()`: Apply colors, backgrounds, and text effects
  - `format()`: Parse and render markup-style tags
  - `create()`: Define custom style tags
  - `delete()`: Remove custom styles
  - `strip()`: Remove markup tags from text
  - `clean()`: Remove ANSI codes from text
  - `length()`: Calculate visible text length

- Cross-platform support
  - Automatic ANSI support on Windows
  - `NO_COLOR` and `FORCE_COLOR` environment variable support
  - TTY detection for appropriate styling

- Color support
  - 16 named ANSI colors (8 standard + 8 bright variants)
  - 24-bit true color (hex codes and RGB tuples)
  - Background colors
  - 8 text effects (bold, dim, italic, underline, blink, reverse, hidden, strikethrough)

- Theme system
  - `set_theme()`: Apply predefined or custom themes
  - Built-in "dark" and "light" themes
  - `temporary()`: Context manager for temporary styles

- Configuration
  - `enable()`, `disable()`: Global style control
  - Predefined style tags for all colors and effects

### Documentation
- Comprehensive README with examples
- Full API documentation
- Color theory and accessibility guides
- Usage examples for all features
