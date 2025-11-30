# Quick Reference

A comprehensive index of all functions, methods, and classes in the Vargula library. Click any item to jump to its full documentation in the API reference.

---

## Instance Creation

| Function | Description |
|----------|-------------|
| [Vargula()](api.md#vargula) | Create an instance of Vargula to access its methods |

## Core Styling Functions


| Function | Description |
|----------|-------------|
| [style()](api.md#style) | Apply styling to text directly with colors and text decorations |
| [format()](api.md#format) | Format text using HTML-like markup tags for inline styling |
| [create()](api.md#create) | Create a custom reusable style tag for use with format() |
| [delete()](api.md#delete) | Delete a previously created custom style tag |
| [write()](api.md#write) | Format and print text with markup in one call |
| [strip()](api.md#strip) | Remove all markup tags from text, leaving only plain text |
| [clean()](api.md#clean) | Remove all ANSI escape codes from text |
| [length()](api.md#length) | Calculate the visible length of text, ignoring ANSI escape codes |
| [enable()](api.md#enable--disable) | Globally enable all styling output |
| [disable()](api.md#enable--disable) | Globally disable all styling output |
| [temporary()](api.md#temporary) | Context manager for temporary custom styles |

---

## Theme Functions

| Function | Description |
|----------|-------------|
| [set_theme()](api.md#set_theme) | Set a predefined or custom theme for consistent styling |

---

## Table Functions

| Class/Method | Description |
|--------------|-------------|
| [Table()](api.md#table) | Create a Rich-style table with extensive customization options |
| [Table.add_column()](api.md#tableadd_column) | Add a column definition to the table |
| [Table.add_row()](api.md#tableadd_row) | Add a row of data to the table |

---

## Progress Bar Functions

| Class/Method/Function | Description |
|-----------------------|-------------|
| [ProgressBar()](api.md#progressbar) | Create a customizable progress bar for tracking operations |
| [ProgressBar.update()](api.md#progressbarupdate) | Update the progress bar by advancing it n steps |
| [ProgressBar.close()](api.md#progressbarclose) | Complete and close the progress bar |
| [progress_bar()](api.md#progress_bar) | Wrap an iterable with a progress bar for automatic tracking |
| [MultiProgress()](api.md#multiprogress) | Manage multiple progress bars simultaneously |
| [MultiProgress.add_task()](api.md#multiprogressadd_task) | Add a new progress task to the multi-progress display |
| [MultiProgress.update()](api.md#multiprogressupdate) | Update a specific task in the multi-progress display |

---

## Color Palette Generation

| Function | Description |
|----------|-------------|
| [generate_palette()](api.md#generate_palette) | Generate a color palette based on color theory principles |
| [generate_theme_palette()](api.md#generate_theme_palette) | Generate a complete theme with semantic color names |
| [generate_accessible_theme()](api.md#generate_accessible_theme) | Generate a theme with colors validated for WCAG contrast |
| [preview_palette()](api.md#preview_palette) | Generate a visual text preview of a color palette |
| [apply_palette_theme()](api.md#apply_palette_theme) | Apply a generated palette as the active theme |

---

## Color Manipulation Functions

| Function | Description |
|----------|-------------|
| [lighten()](api.md#lighten) | Increase the brightness (value in HSV) of a color |
| [darken()](api.md#darken) | Decrease the brightness (value in HSV) of a color |
| [saturate()](api.md#saturate) | Increase the saturation of a color, making it more vivid |
| [desaturate()](api.md#desaturate) | Decrease the saturation of a color, making it more gray |
| [shift_hue()](api.md#shift_hue) | Rotate the hue of a color by specified degrees on the color wheel |
| [invert()](api.md#invert) | Invert a color by flipping its RGB values |
| [mix()](api.md#mix) | Mix two colors together with a specified weight |

---

## Accessibility Functions

| Function | Description |
|----------|-------------|
| [calculate_contrast_ratio()](api.md#calculate_contrast_ratio) | Calculate WCAG 2.1 contrast ratio between two colors |
| [meets_wcag()](api.md#meets_wcag) | Check if two colors meet WCAG contrast requirements |
| [ensure_contrast()](api.md#ensure_contrast) | Automatically adjust a foreground color to meet minimum contrast |

---

## Color Blindness Functions

| Function | Description |
|----------|-------------|
| [simulate_colorblindness()](api.md#simulate_colorblindness) | Simulate how a color appears to individuals with color blindness |
| [validate_colorblind_safety()](api.md#validate_colorblind_safety) | Check if colors in a palette remain distinguishable |

---

## Persistence Functions

| Function | Description |
|----------|-------------|
| [save_palette()](api.md#save_palette) | Save a color palette to a JSON file |
| [load_palette()](api.md#load_palette) | Load a color palette from a JSON file |
| [save_theme()](api.md#save_theme) | Save a theme palette to a JSON file |
| [load_theme()](api.md#load_theme) | Load a theme palette from a JSON file |

---

## Function Categories

### By Use Case

**Instance Creation:**
- [Vargula()](api.md#vargula) - Creating an instance of Vargula

**Text Styling:**
- [style()](api.md#style) - Direct styling
- [format()](api.md#format) - Markup-based styling
- [write()](api.md#write) - Print with styling

**Style Management:**
- [create()](api.md#create) - Create custom styles
- [delete()](api.md#delete) - Remove custom styles
- [temporary()](api.md#temporary) - Temporary styles
- [set_theme()](api.md#set_theme) - Apply themes

**Text Processing:**
- [strip()](api.md#strip) - Remove markup
- [clean()](api.md#clean) - Remove ANSI codes
- [length()](api.md#length) - Get visible length

**UI Components:**
- [Table()](api.md#table) - Data tables
- [ProgressBar()](api.md#progressbar) - Single progress bar
- [MultiProgress()](api.md#multiprogress) - Multiple progress bars

**Color Generation:**
- [generate_palette()](api.md#generate_palette) - Basic palettes
- [generate_theme_palette()](api.md#generate_theme_palette) - Semantic themes
- [generate_accessible_theme()](api.md#generate_accessible_theme) - WCAG-compliant themes

**Color Editing:**
- [lighten()](api.md#lighten), [darken()](api.md#darken) - Brightness
- [saturate()](api.md#saturate), [desaturate()](api.md#desaturate) - Saturation
- [shift_hue()](api.md#shift_hue) - Hue rotation
- [invert()](api.md#invert) - Color inversion
- [mix()](api.md#mix) - Color mixing

**Accessibility:**
- [calculate_contrast_ratio()](api.md#calculate_contrast_ratio) - Measure contrast
- [meets_wcag()](api.md#meets_wcag) - Validate compliance
- [ensure_contrast()](api.md#ensure_contrast) - Auto-adjust colors
- [simulate_colorblindness()](api.md#simulate_colorblindness) - Simulate vision
- [validate_colorblind_safety()](api.md#validate_colorblind_safety) - Check palette

**Data Persistence:**
- [save_palette()](api.md#save_palette), [load_palette()](api.md#load_palette) - Palettes
- [save_theme()](api.md#save_theme), [load_theme()](api.md#load_theme) - Themes

---

## Alphabetical Index

| A-D | E-L | M-S | T-Z |
|-----|-----|-----|-----|
| [apply_palette_theme()](api.md#apply_palette_theme) | [enable()](api.md#enable--disable) | [meets_wcag()](api.md#meets_wcag) | [Table()](api.md#table) |
| [calculate_contrast_ratio()](api.md#calculate_contrast_ratio) | [ensure_contrast()](api.md#ensure_contrast) | [mix()](api.md#mix) | [Table.add_column()](api.md#tableadd_column) |
| [clean()](api.md#clean) | [format()](api.md#format) | [MultiProgress()](api.md#multiprogress) | [Table.add_row()](api.md#tableadd_row) |
| [create()](api.md#create) | [generate_accessible_theme()](api.md#generate_accessible_theme) | [MultiProgress.add_task()](api.md#multiprogressadd_task) | [temporary()](api.md#temporary) |
| [darken()](api.md#darken) | [generate_palette()](api.md#generate_palette) | [MultiProgress.update()](api.md#multiprogressupdate) | [validate_colorblind_safety()](api.md#validate_colorblind_safety) |
| [delete()](api.md#delete) | [generate_theme_palette()](api.md#generate_theme_palette) | [preview_palette()](api.md#preview_palette) | [write()](api.md#write) |
| [desaturate()](api.md#desaturate) | [invert()](api.md#invert) | [progress_bar()](api.md#progress_bar) | |
| [disable()](api.md#enable--disable) | [length()](api.md#length) | [ProgressBar()](api.md#progressbar) | |
| | [lighten()](api.md#lighten) | [ProgressBar.close()](api.md#progressbarclose) | |
| | [load_palette()](api.md#load_palette) | [ProgressBar.update()](api.md#progressbarupdate) | |
| | [load_theme()](api.md#load_theme) | [saturate()](api.md#saturate) | |
| | | [save_palette()](api.md#save_palette) | |
| | | [save_theme()](api.md#save_theme) | |
| | | [set_theme()](api.md#set_theme) | |
| | | [shift_hue()](api.md#shift_hue) | |
| | | [simulate_colorblindness()](api.md#simulate_colorblindness) | |
| | | [strip()](api.md#strip) | |
| | | [style()](api.md#style) | |

---

## Common Workflows

### Basic Text Styling
1. [style()](api.md#style) - For simple, direct styling
2. [format()](api.md#format) - For markup-based styling
3. [write()](api.md#write) - For styled printing

### Custom Style System
1. [create()](api.md#create) - Define custom styles
2. [format()](api.md#format) - Use custom styles
3. [delete()](api.md#delete) - Clean up when done

### Theme Creation
1. [generate_theme_palette()](api.md#generate_theme_palette) - Generate theme
2. [preview_palette()](api.md#preview_palette) - Preview colors
3. [apply_palette_theme()](api.md#apply_palette_theme) - Apply theme
4. [save_theme()](api.md#save_theme) - Save for later

### Accessible Design
1. [generate_accessible_theme()](api.md#generate_accessible_theme) - Create compliant theme
2. [calculate_contrast_ratio()](api.md#calculate_contrast_ratio) - Verify contrast
3. [meets_wcag()](api.md#meets_wcag) - Check compliance
4. [simulate_colorblindness()](api.md#simulate_colorblindness) - Test visibility

### Data Visualization
1. [Table()](api.md#table) - Create table
2. [Table.add_column()](api.md#tableadd_column) - Define columns
3. [Table.add_row()](api.md#tableadd_row) - Add data

### Progress Tracking
1. [ProgressBar()](api.md#progressbar) - Create progress bar
2. [ProgressBar.update()](api.md#progressbarupdate) - Update progress
3. [ProgressBar.close()](api.md#progressbarclose) - Finish

---

## Quick Start Examples

### Styling Text
```python
from vargula import Vargula
vg = Vargula()

# Direct styling
print(vg.style("Error", color="red", look="bold"))

# Markup styling
print(vg.format("This is <red>red</red> and <bold>bold</bold>"))

# Custom styles
vg.create("error", color="red", look="bold")
print(vg.format("<error>Error!</error>"))
```

### Creating Tables
```python
table = vg.Table(title="Report")
table.add_column("Name", style="cyan")
table.add_column("Score", style="green", justify="right")
table.add_row("Alice", "95")
table.add_row("Bob", "87")
print(table)
```

### Progress Bars
```python
import time

# Simple progress bar
for i in vg.progress_bar(range(100), desc="Processing"):
    time.sleep(0.01)

# Multiple progress bars
with vg.MultiProgress() as mp:
    task1 = mp.add_task("Download", total=100)
    task2 = mp.add_task("Extract", total=50)
    # ... update tasks
```

### Color Palettes
```python
# Generate palette
colors = vg.generate_palette("#3498db", "complementary", 5)

# Preview colors
print(vg.preview_palette(colors))

# Create theme
theme = vg.generate_theme_palette("analogous", "#e74c3c")
vg.apply_palette_theme(theme)
```

---

## Parameter Quick Reference

### Common Parameters

**Color Parameters:** (used in style(), create(), etc.)
- `color` - Foreground color (name, hex, or RGB tuple)
- `bg` - Background color (name, hex, or RGB tuple)

**Look Parameters:**
- `look` - Text decoration(s) (string or list)
  - Options: `bold`, `dim`, `italic`, `underline`, `blink`, `reverse`, `hidden`, `strikethrough`

**Table Parameters:**
- `title` - Table title
- `caption` - Table caption
- `style` - Default cell style
- `box` - Border style: `"rounded"`, `"square"`, `"double"`, `"heavy"`, `"minimal"`, `"none"`
- `show_header` - Display header row (bool)
- `show_lines` - Show lines between rows (bool)
- `padding` - Cell padding as (vertical, horizontal)
- `expand` - Expand to full width (bool)

**Progress Bar Parameters:**
- `total` - Total iterations
- `desc` - Description text
- `unit` - Unit name (e.g., "files", "items")
- `bar_width` - Width in characters
- `show_percentage` - Display percentage (bool)
- `show_count` - Display count (bool)
- `show_rate` - Display rate (bool)
- `show_eta` - Display ETA (bool)

**Palette Generation Parameters:**
- `base_color` - Starting hex color
- `scheme` - Color harmony scheme
- `count` - Number of colors to generate
- `saturation_range` - Min/max saturation (0-1)
- `value_range` - Min/max brightness (0-1)

**WCAG Parameters:**
- `level` - Compliance level: `"AA"` or `"AAA"`
- `large_text` - Text is 18pt+ or 14pt+ bold (bool)
- `min_contrast` - Minimum contrast ratio (float)

---

## Return Type Quick Reference

| Function | Returns |
|----------|---------|
| [style()](api.md#style) | `str` - Styled string with ANSI codes |
| [format()](api.md#format) | `str` - Formatted string with ANSI codes |
| [create()](api.md#create) | `None` |
| [delete()](api.md#delete) | `bool` - True if deleted, False if not found |
| [write()](api.md#write) | `None` - Prints to stdout |
| [strip()](api.md#strip) | `str` - Plain text without markup |
| [clean()](api.md#clean) | `str` - Plain text without ANSI codes |
| [length()](api.md#length) | `int` - Visible character count |
| [generate_palette()](api.md#generate_palette) | `list[str]` - List of hex colors |
| [generate_theme_palette()](api.md#generate_theme_palette) | `dict` - Theme dictionary |
| [generate_accessible_theme()](api.md#generate_accessible_theme) | `dict` - Theme dictionary |
| [preview_palette()](api.md#preview_palette) | `str` - Formatted preview string |
| [lighten()](api.md#lighten) | `str` - Hex color |
| [darken()](api.md#darken) | `str` - Hex color |
| [saturate()](api.md#saturate) | `str` - Hex color |
| [desaturate()](api.md#desaturate) | `str` - Hex color |
| [shift_hue()](api.md#shift_hue) | `str` - Hex color |
| [invert()](api.md#invert) | `str` - Hex color |
| [mix()](api.md#mix) | `str` - Hex color |
| [calculate_contrast_ratio()](api.md#calculate_contrast_ratio) | `float` - Contrast ratio (1-21) |
| [meets_wcag()](api.md#meets_wcag) | `bool` - Compliance status |
| [ensure_contrast()](api.md#ensure_contrast) | `str` - Adjusted hex color |
| [simulate_colorblindness()](api.md#simulate_colorblindness) | `str` - Simulated hex color |
| [validate_colorblind_safety()](api.md#validate_colorblind_safety) | `tuple` - (bool, list of problems) |
| [load_palette()](api.md#load_palette) | `tuple` - (colors list, metadata dict) |
| [load_theme()](api.md#load_theme) | `tuple` - (theme dict, metadata dict) |
| [MultiProgress.add_task()](api.md#multiprogressadd_task) | `int` - Task ID |



---

**Last Updated:** 2025-11-30  
**Library Version:** 2.0.0