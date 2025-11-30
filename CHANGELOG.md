# Changelog

All notable changes to the vargula project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-11-30

### BREAKING CHANGES
- **API Restructured to Class-Based Design**: Major refactoring for better organization and thread-safety
  - All functionality now accessed through `Vargula` class instances
  - Removed module-level global functions (global state eliminated)
  - Each instance maintains independent state for thread-safe operations

### Changed
- **Module API**: Changed from functional to object-oriented
  ```python
  # Old (v1.x)
  import vargula as vg
  vg.style("text", color="red")
  vg.create("error", color="red")
  vg.format("<error>Error</error>")
  
  # New (v2.0)
  from vargula import Vargula
  vg = Vargula()
  vg.style("text", color="red")
  vg.create("error", color="red")
  vg.format("<error>Error</error>")
  ```

- **Rich Components API**: Table and ProgressBar now factory methods
  ```python
  # Old (v1.x)
  from vargula import Table, ProgressBar
  table = Table(title="Users")
  pbar = ProgressBar(total=100)
  
  # New (v2.0)
  vg = Vargula()
  table = vg.Table(title="Users")
  pbar = vg.ProgressBar(total=100)
  ```

- **Inner Classes**: `Table`, `ProgressBar`, and `MultiProgress` now accessed as factory methods
  - Cleaner API with implicit Vargula instance
  - Returns properly typed inner class instances

### Added
- **Instance-based styling**: Each `Vargula()` instance has independent state
  - Custom styles isolated per instance
  - Theme configuration per instance
  - Multiple instances can coexist without interference
  
- **Factory Methods**: Convenient creation of rich components
  - `vg.Table()`: Create styled tables
  - `vg.ProgressBar()`: Create progress bars
  - `vg.MultiProgress()`: Create multi-task progress manager

### Benefits
- **Thread-Safe**: No global state, instances can be used in concurrent environments
- **Better Organization**: All functionality logically grouped under instance
- **Easier Testing**: No global state to manage
- **Multiple Themes**: Use different themes in different instances simultaneously

### Migration Guide

#### Basic Styling
```python
# v1.x
import vargula as vg
styled = vg.style("Hello", color="red", look="bold")

# v2.0
from vargula import Vargula
vg = Vargula()
styled = vg.style("Hello", color="red", look="bold")
```

#### Custom Styles
```python
# v1.x
vg.create("error", color="red", look="bold")
vg.format("<error>Error occurred</error>")

# v2.0
vg = Vargula()
vg.create("error", color="red", look="bold")
vg.format("<error>Error occurred</error>")
```

#### Tables
```python
# v1.x
from vargula import Table
table = Table(title="Users")
table.add_column("Name")
table.add_row("Alice")

# v2.0
vg = Vargula()
table = vg.Table(title="Users")
table.add_column("Name")
table.add_row("Alice")
```

#### Progress Bars
```python
# v1.x
from vargula import ProgressBar
with ProgressBar(total=100, desc="Processing") as pbar:
    for i in range(100):
        pbar.update(1)

# v2.0
vg = Vargula()
with vg.ProgressBar(total=100, desc="Processing") as pbar:
    for i in range(100):
        pbar.update(1)
```

#### Color Palettes
```python
# v1.x
import vargula as vg
palette = vg.generate_palette("#3498db", "complementary", 5)
theme = vg.generate_theme_palette("analogous", "#e74c3c")

# v2.0
vg = Vargula()
palette = vg.generate_palette("#3498db", "complementary", 5)
theme = vg.generate_theme_palette("analogous", "#e74c3c")
```

### Documentation
- Updated all examples to use class-based API
- Added instance creation patterns
- Thread-safety documentation

## [1.1.0] - 2024-11-24

### Added
- **Escape sequences**: Support for literal tag display
  - Use `r'\<'` to show literal `<` in tags
  - Use `r'\>'` to show literal `>` in tags
  - Enables documentation and tutorial content with visible markup syntax
  - Works in both global API and instance methods

### Examples

#### Escape Sequences
```python
import vargula as vg

# Show literal tags in documentation
vg.write(r"Use \<red>text\</red> to make text red")
# Output: Use <red>text</red> to make text red

# Mix literal and styled tags
vg.write(r"Example: \<bold>syntax\</bold> creates <bold>bold</bold> text")
# Output: Example: <bold>syntax</bold> creates [bold]bold[/bold] text

# Tutorial content
vg.create("syntax", color="yellow")
vg.write(r"Tag syntax: \<syntax>highlighted code\</syntax> becomes <syntax>highlighted code</syntax>")
```

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