# Vargula API 

A comprehensive Python library for terminal text styling, formatting, and UI components.

---

## Core Styling Functions

### style()

**Function:** `style(text, color=None, bg=None, look=None)`

Apply styling to text directly with colors and text decorations.

**Parameters:**
- `text` (str): Text to style
- `color` (str|tuple): Foreground color - accepts color name, hex string (e.g., `"#FF5733"`), or RGB tuple (e.g., `(255, 87, 51)`)
- `bg` (str|tuple): Background color - same format options as `color`
- `look` (str|list): Text decoration(s) - single string or list of decorations

**Returns:** `str` - Styled string with ANSI escape codes

**Available Colors:**
- **Basic:** `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`
- **Bright:** `bright_black`, `bright_red`, `bright_green`, `bright_yellow`, `bright_blue`, `bright_magenta`, `bright_cyan`, `bright_white`

**Available Looks:**
- `bold`, `dim`, `italic`, `underline`, `blink`, `reverse`, `hidden`, `strikethrough`

**Examples:**

```python
import vargula as vg

# Named colors
print(vg.style("Error", color="red", look="bold"))

# Hex colors
print(vg.style("Custom", color="#FF5733", bg="#1a1a1a"))

# RGB tuples
print(vg.style("RGB", color=(255, 87, 51)))

# Multiple looks
print(vg.style("Fancy", color="cyan", look=["bold", "underline"]))
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-43-36.png?raw=true)

---

### format()

**Function:** `format(text)`

Format text using HTML-like markup tags for inline styling.

**Parameters:**
- `text` (str): Text containing markup tags (e.g., `<red>text</red>`)

**Returns:** `str` - Formatted string with ANSI codes applied

**Examples:**

```python
# Using predefined color tags
print(vg.format("This is <red>red</red> and <blue>blue</blue>"))

# Using custom styles (see create())
vg.create("error", color="red", look="bold")
print(vg.format("An <error>error</error> occurred"))

# Nested tags
print(vg.format("<bold>Bold with <red>red text</red></bold>"))

# Hex colors directly
print(vg.format("Hex <#FF5733>color</#FF5733>"))

# Combined styles
print(vg.format("<bold><underline><cyan>Triple style</cyan></underline></bold>"))
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-46-26.png?raw=true)

---

### create()

**Function:** `create(name, color=None, bg=None, look=None)`

Create a custom reusable style tag for use with `format()`.

**Parameters:**
- `name` (str): Name of the custom style tag
- `color` (str|tuple): Foreground color
- `bg` (str|tuple): Background color
- `look` (str|list): Text decoration(s)

**Returns:** `None`

**Examples:**

```python
# Create custom styles
vg.create("error", color="red", look="bold")
vg.create("success", color="green", look="bold")
vg.create("highlight", bg="yellow", color="black")

# Use them with format()
print(vg.format("<error>Error!</error>"))
print(vg.format("<success>Success!</success>"))
print(vg.format("<highlight>Important</highlight>"))
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-48-45.png?raw=true)

---

### delete()

**Function:** `delete(name)`

Delete a previously created custom style tag.

**Parameters:**
- `name` (str): Name of the style to delete

**Returns:** `bool` - `True` if style was found and deleted, `False` if style didn't exist

**Example:**

```python
vg.create("temp", color="blue")
vg.delete("temp")  # Returns True
vg.delete("temp")  # Returns False (already deleted)
```

---

### write()

**Function:** `write(*args, sep=" ", end="\n", file=None, flush=False)`

Format and print text with markup in one call. Works exactly like Python's built-in `print()` but automatically formats markup tags.

**Parameters:**
- `*args`: Values to print (will be converted to strings and formatted)
- `sep` (str): String inserted between values (default: `" "`)
- `end` (str): String appended after the last value (default: `"\n"`)
- `file`: File object where output is written (default: `sys.stdout`)
- `flush` (bool): Whether to forcibly flush the stream (default: `False`)

**Returns:** `None` (prints to stdout or specified file)

**Examples:**

```python
# Basic usage
vg.write("This is <red>red</red> and <bold>bold</bold>")

# Multiple arguments with custom separator
vg.write("Hello", "<red>World</red>", sep=" → ")
# Output: Hello → World (with "World" in red)

# Formatted separator
vg.write("user", "localhost", sep=vg.format("<cyan>@</cyan>"))
# Output: user@localhost (with @ in cyan)

# Custom end character
vg.write("<bold>Processing</bold>", end="... ")
vg.write("<green>Done!</green>")
# Output: Processing... Done! (on same line)
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2016-35-49.png?raw=true)

---

### strip()

**Function:** `strip(text)`

Remove all markup tags from text, leaving only plain text.

**Parameters:**
- `text` (str): Text containing markup tags

**Returns:** `str` - Plain text without any markup tags

**Example:**

```python
text = "Hello <red>world</red>!"
plain = vg.strip(text)  # Returns: "Hello world!"
```

---

### clean()

**Function:** `clean(text)`

Remove all ANSI escape codes from text.

**Parameters:**
- `text` (str): Text containing ANSI escape codes

**Returns:** `str` - Plain text without ANSI codes

**Example:**

```python
styled = vg.style("Colored", color="red")
plain = vg.clean(styled)  # Returns: "Colored" (no ANSI codes)
```

---

### length()

**Function:** `length(text)`

Calculate the visible length of text, ignoring ANSI escape codes.

**Parameters:**
- `text` (str): Text with ANSI codes

**Returns:** `int` - Visible character count

**Example:**

```python
styled = vg.style("Hello", color="red")
print(len(styled))        # 18 (includes ANSI codes)
print(vg.length(styled))  # 5 (visible length only)
```

---

### enable() / disable()

**Functions:** `enable()` and `disable()`

Globally enable or disable all styling output. When disabled, all styling functions return plain text.

**Parameters:** None

**Returns:** `None`

**Example:**

```python
vg.disable()
print(vg.style("No color", color="red"))  # Prints plain text without color

vg.enable()
print(vg.style("Has color", color="red"))  # Prints colored text
```

---

### temporary()

**Function:** `temporary(name, color=None, bg=None, look=None)`

Context manager for temporary custom styles that are automatically deleted when exiting the context.

**Parameters:**
- `name` (str): Name of the temporary style
- `color` (str|tuple): Foreground color
- `bg` (str|tuple): Background color
- `look` (str|list): Text decoration(s)

**Returns:** Context manager object

**Example:**

```python
with vg.temporary("temp", color="cyan", look="bold"):
    print(vg.format("<temp>Temporary style</temp>"))
# "temp" style is automatically deleted after the block
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-51-49.png?raw=true)

---

## Theme Functions

### set_theme()

**Function:** `set_theme(theme)`

Set a predefined or custom theme for consistent styling across your application.

**Parameters:**
- `theme` (str|dict): Either a built-in theme name (`"dark"`, `"light"`) or a custom theme dictionary

**Returns:** `None`

**Built-in Theme Styles:**

When using built-in themes, the following style tags become available:
- `error` - Error messages
- `success` - Success messages
- `warning` - Warning messages
- `info` - Informational messages
- `debug` - Debug output
- `critical` - Critical alerts

**Example:**

```python
# Built-in dark theme
vg.set_theme("dark")
print(vg.format("<error>Error!</error> <success>OK</success>"))

# Built-in light theme
vg.set_theme("light")
print(vg.format("<warning>Warning</warning>"))

# Custom theme
custom = {
    "error": {"color": "red", "look": "bold"},
    "info": {"color": "blue"},
    "highlight": {"bg": "yellow", "color": "black"}
}
vg.set_theme(custom)
print(vg.format("<error>Custom error style</error>"))
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-53-57.png?raw=true)

---

## Tables

### Table()

**Class:** `Table(title=None, caption=None, **kwargs)`

Create a Rich-style table with extensive customization options.

**Parameters:**
- `title` (str, optional): Title displayed above the table
- `caption` (str, optional): Caption displayed below the table
- `style` (str, optional): Default style applied to all cells
- `title_style` (str): Style for title text (default: `"bold"`)
- `caption_style` (str): Style for caption text (default: `"dim"`)
- `header_style` (str): Style for header row (default: `"bold"`)
- `border_style` (str, optional): Style for border characters
- `show_header` (bool): Whether to display the header row (default: `True`)
- `show_lines` (bool): Whether to show lines between rows (default: `False`)
- `padding` (tuple): Vertical and horizontal padding as `(vertical, horizontal)` (default: `(0, 1)`)
- `expand` (bool): Expand table to full terminal width (default: `False`)
- `min_width` (int, optional): Minimum table width in characters
- `box` (str): Border style (default: `"rounded"`)

**Box Styles:**
- `"rounded"` - Rounded corners (╭─╮)
- `"square"` - Square corners (┌─┐)
- `"double"` - Double-line borders (╔═╗)
- `"heavy"` - Heavy-line borders (┏━┓)
- `"minimal"` - Minimal borders
- `"none"` - No borders

**Example:**

```python
table = vg.Table(
    title="Sales Report",
    caption="Q4 2024",
    title_style="bold cyan",
    border_style="blue",
    show_lines=True,
    box="double"
)

table.add_column("Region", style="cyan", justify="left")
table.add_column("Revenue", style="green", justify="right")
table.add_column("Growth", style="yellow", justify="center")

table.add_row("North", "$1.2M", "+15%")
table.add_row("South", "$890K", "+8%", style="dim")
table.add_row("East", "$1.5M", "+22%")

print(table)
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-54-28.png?raw=true)

---

### Table.add_column()

**Method:** `add_column(header, style=None, justify="left", **kwargs)`

Add a column definition to the table. Must be called before adding rows.

**Parameters:**
- `header` (str): Column header text
- `style` (str, optional): Style applied to all cells in this column
- `justify` (str): Text alignment - `"left"`, `"center"`, or `"right"` (default: `"left"`)
- `no_wrap` (bool): Disable text wrapping in this column (default: `False`)
- `overflow` (str): How to handle overflow - `"ellipsis"`, `"crop"`, or `"fold"`
- `width` (int, optional): Fixed column width in characters
- `min_width` (int, optional): Minimum column width
- `max_width` (int, optional): Maximum column width

**Returns:** `None`

**Example:**

```python
table.add_column("Name", style="bold", justify="left", width=20)
table.add_column("Score", style="green", justify="right", max_width=10)
table.add_column("Status", justify="center")
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-54-47.png?raw=true)

---

### Table.add_row()

**Method:** `add_row(*cells, style=None)`

Add a row of data to the table.

**Parameters:**
- `*cells`: Cell values as separate arguments (one per column, in column order)
- `style` (str, optional): Style for this entire row (overrides column styles)

**Returns:** `None`

**Example:**

```python
table.add_row("Alice", "95", "Active")
table.add_row("Bob", "87", "Active", style="dim")  # Entire row dimmed
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-55-08.png?raw=true)

---

## Progress Bars

### ProgressBar()

**Class:** `ProgressBar(total=100, desc="", **kwargs)`

Create a customizable progress bar for tracking long-running operations.

**Parameters:**
- `total` (int): Total number of iterations (default: `100`)
- `desc` (str): Description text displayed before the progress bar (default: `""`)
- `unit` (str): Unit name for items being processed (e.g., `"files"`, `"items"`, `"it"`)
- `bar_width` (int): Width of the progress bar in characters (default: `40`)
- `complete_style` (str): Style for completed portion of bar (default: `"green"`)
- `incomplete_style` (str): Style for incomplete portion (default: `"bright_black"`)
- `percentage_style` (str): Style for percentage display (default: `"cyan"`)
- `desc_style` (str): Style for description text (default: `"bold"`)
- `show_percentage` (bool): Display percentage complete (default: `True`)
- `show_count` (bool): Display current/total count (default: `True`)
- `show_rate` (bool): Display processing rate (default: `True`)
- `show_eta` (bool): Display estimated time remaining (default: `True`)
- `refresh_rate` (float): Minimum seconds between display updates (default: `0.1`)

**Example:**

```python
import time

progress = vg.ProgressBar(
    total=500,
    desc="Downloading",
    unit="files",
    bar_width=50,
    complete_style="green",
    desc_style="bold cyan"
)

for i in range(500):
    # Do work
    time.sleep(0.01)
    progress.update(1)

progress.close()
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2007-57-51.gif?raw=true)

---

### ProgressBar.update()

**Method:** `update(n=1)`

Update the progress bar by advancing it n steps.

**Parameters:**
- `n` (int): Number of steps to advance (default: `1`)

**Returns:** `None`

**Example:**

```python
pbar = vg.ProgressBar(total=100)
pbar.update(1)   # Advance by 1 step
pbar.update(10)  # Advance by 10 steps
```

---

### ProgressBar.close()

**Method:** `close()`

Complete and close the progress bar, ensuring the final state is displayed.

**Returns:** `None`

**Example:**

```python
pbar = vg.ProgressBar(total=100)
# ... perform work ...
pbar.close()  # Ensures final 100% state is displayed
```

---

### progress_bar()

**Function:** `progress_bar(iterable, total=None, desc="", **kwargs)`

Wrap an iterable with a progress bar for automatic tracking.

**Parameters:**
- `iterable`: Any iterable object (list, range, generator, etc.)
- `total` (int, optional): Total count (auto-detected if the iterable has `__len__`)
- `desc` (str): Description text
- `**kwargs`: Additional arguments passed to `ProgressBar()`

**Returns:** Iterator that yields items from the iterable

**Example:**

```python
import time

# Progress bar automatically updates as you iterate
for item in vg.progress_bar(range(100), desc="Processing"):
    # Process item
    time.sleep(0.01)
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-00-53.gif?raw=true)

---

### MultiProgress()

**Class:** `MultiProgress()`

Manage multiple progress bars simultaneously with automatic layout management.

**Example:**

```python
import time

with vg.MultiProgress() as mp:
    task1 = mp.add_task("Download", total=100)
    task2 = mp.add_task("Extract", total=50)
    task3 = mp.add_task("Process", total=75)
    
    for i in range(100):
        mp.update(task1, 1)
        if i % 2 == 0:
            mp.update(task2, 1)
        if i % 3 == 0:
            mp.update(task3, 1)
        time.sleep(0.02)
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-03-51.gif?raw=true)

---

### MultiProgress.add_task()

**Method:** `add_task(desc, total=100, **kwargs)`

Add a new progress task to the multi-progress display.

**Parameters:**
- `desc` (str): Task description
- `total` (int): Total number of iterations (default: `100`)
- `**kwargs`: Additional arguments passed to `ProgressBar()`

**Returns:** `int` - Task ID for use with `update()`

---

### MultiProgress.update()

**Method:** `update(task_id, n=1)`

Update a specific task in the multi-progress display.

**Parameters:**
- `task_id` (int): ID returned from `add_task()`
- `n` (int): Number of steps to advance (default: `1`)

**Returns:** `None`

---

## Color Palette Generation

### generate_palette()

**Function:** `generate_palette(base_color=None, scheme="random", count=5, **kwargs)`

Generate a color palette based on color theory principles.

**Parameters:**
- `base_color` (str, optional): Starting hex color (e.g., `"#FF5733"`). If `None`, a random color is chosen
- `scheme` (str): Color harmony scheme (default: `"random"`)
- `count` (int): Number of colors to generate (default: `5`)
- `saturation_range` (tuple): Min and max saturation as `(min, max)` where values are 0-1 (default: `(0.4, 1.0)`)
- `value_range` (tuple): Min and max brightness as `(min, max)` where values are 0-1 (default: `(0.4, 1.0)`)
- `randomize` (bool): Add slight random variations to colors (default: `True`)

**Returns:** `list[str]` - List of hex color strings

**Color Harmony Schemes:**
- `"monochromatic"` - Variations of a single hue
- `"analogous"` - Adjacent hues on color wheel (±30°)
- `"complementary"` - Opposite hues (180°)
- `"triadic"` - Three evenly spaced hues (120° apart)
- `"tetradic"` - Four hues at 60°, 180°, 240°
- `"split_complementary"` - Base color plus two adjacent to its complement
- `"square"` - Four evenly spaced hues (90° apart)
- `"random"` - Randomly selected colors

**Examples:**

```python
# Complementary palette from blue
colors = vg.generate_palette("#3498db", "complementary", 5)
# Returns: ['#3498db', '#db7834', '#34a4db', '#db3449', '#4ddb34']

# Random palette
colors = vg.generate_palette(scheme="random", count=8)

# Analogous palette with custom ranges
colors = vg.generate_palette(
    base_color="#e74c3c",
    scheme="analogous",
    count=6,
    saturation_range=(0.6, 0.9),
    value_range=(0.6, 0.95)
)
```

---

### generate_theme_palette()

**Function:** `generate_theme_palette(scheme="random", base_color=None, **kwargs)`

Generate a complete theme with semantic color names suitable for UI applications.

**Parameters:**
- `scheme` (str): Color harmony scheme (default: `"random"`)
- `base_color` (str, optional): Optional base hex color to start from
- `include_neutrals` (bool): Add grayscale background/foreground colors (default: `True`)
- `force_semantic_colors` (bool): Use standard colors for success/warning/error regardless of scheme (default: `False`)

**Returns:** `dict` - Dictionary mapping theme names to hex colors

**Theme Keys:**

The returned dictionary contains these keys:
- `primary` - Primary brand color
- `secondary` - Secondary brand color
- `accent` - Accent color for highlights
- `success` - Success state color (usually green)
- `warning` - Warning state color (usually yellow/orange)
- `error` - Error state color (usually red)
- `info` - Information color (usually blue)
- `background` - Background color (when `include_neutrals=True`)
- `foreground` - Foreground/text color (when `include_neutrals=True`)

**Example:**

```python
theme = vg.generate_theme_palette("complementary", "#3498db")
# Returns:
# {
#     'primary': '#3498db',
#     'secondary': '#db7834',
#     'accent': '#34dbb4',
#     'success': '#2ecc71',
#     'warning': '#f39c12',
#     'error': '#e74c3c',
#     'info': '#3498db',
#     'background': '#1a1a1a',
#     'foreground': '#e0e0e0'
# }

vg.apply_palette_theme(theme)
print(vg.format("<primary>Primary</primary> <error>Error</error>"))
```

---

### generate_accessible_theme()

**Function:** `generate_accessible_theme(base_color, scheme="complementary", **kwargs)`

Generate a theme with colors validated for WCAG contrast requirements.

**Parameters:**
- `base_color` (str): Base hex color to build theme from
- `scheme` (str): Color harmony scheme (default: `"complementary"`)
- `background` (str): Background hex color to test contrast against (default: `"#1a1a1a"`)
- `min_contrast` (float): Minimum contrast ratio (default: `4.5`)
- `wcag_level` (str): WCAG conformance level - `"AA"` or `"AAA"` (default: `"AA"`)

**Returns:** `dict` - Dictionary with accessible colors that meet contrast requirements

**WCAG Contrast Requirements:**
- **AA Normal Text:** 4.5:1 minimum
- **AA Large Text:** 3:1 minimum
- **AAA Normal Text:** 7:1 minimum
- **AAA Large Text:** 4.5:1 minimum

**Example:**

```python
# All colors will meet WCAG AA contrast on white background
theme = vg.generate_accessible_theme(
    "#3498db",
    scheme="triadic",
    background="#ffffff",
    wcag_level="AA"
)

# Verify colors meet requirements
for name, color in theme.items():
    ratio = vg.calculate_contrast_ratio(color, "#ffffff")
    print(f"{name}: {ratio:.2f}:1")
```

---

### preview_palette()

**Function:** `preview_palette(colors, width=40, show_info=True)`

Generate a visual text preview of a color palette.

**Parameters:**
- `colors` (list): List of hex color strings
- `width` (int): Width of each color block in characters (default: `40`)
- `show_info` (bool): Show HSV values below each color (default: `True`)

**Returns:** `str` - Formatted string with colored blocks

**Example:**

```python
colors = vg.generate_palette("#3498db", "analogous", 5)
print(vg.preview_palette(colors))
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-06-53.png?raw=true)

---

### apply_palette_theme()

**Function:** `apply_palette_theme(palette, register_styles=True)`

Apply a generated palette as the active theme and optionally register each color as a custom style.

**Parameters:**
- `palette` (dict): Dictionary from `generate_theme_palette()`
- `register_styles` (bool): Register each color name as a custom style tag (default: `True`)

**Returns:** `None`

**Example:**

```python
theme = vg.generate_theme_palette("analogous", "#e74c3c")
vg.apply_palette_theme(theme)

# Use theme colors as style tags
print(vg.format("<primary>Primary text</primary>"))
print(vg.format("<success>Success message</success>"))
print(vg.format("<error>Error message</error>"))
```

![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-07-44.png?raw=true)

---

## Color Manipulation

### lighten()

**Function:** `lighten(color, amount=0.1)`

Increase the brightness (value in HSV) of a color.

**Parameters:**
- `color` (str): Hex color string
- `amount` (float): Brightness increase amount between 0 and 1 (default: `0.1`)

**Returns:** `str` - Lightened hex color

**Example:**

```python
lighter = vg.lighten("#3498db", 0.2)  # Returns: '#3cb0ff'
```

---

### darken()

**Function:** `darken(color, amount=0.1)`

Decrease the brightness (value in HSV) of a color.

**Parameters:**
- `color` (str): Hex color string
- `amount` (float): Brightness decrease amount between 0 and 1 (default: `0.1`)

**Returns:** `str` - Darkened hex color

**Example:**

```python
darker = vg.darken("#3498db", 0.2)  # Returns: '#2774a7'
```

---

### saturate()

**Function:** `saturate(color, amount=0.1)`

Increase the saturation of a color, making it more vivid.

**Parameters:**
- `color` (str): Hex color string
- `amount` (float): Saturation increase amount between 0 and 1 (default: `0.1`)

**Returns:** `str` - More saturated hex color

**Example:**

```python
more_saturated = vg.saturate("#80a0c0", 0.3)  # Returns: '#5a9ad8'
```

---

### desaturate()

**Function:** `desaturate(color, amount=0.1)`

Decrease the saturation of a color, making it more gray.

**Parameters:**
- `color` (str): Hex color string
- `amount` (float): Saturation decrease amount between 0 and 1 (default: `0.1`)

**Returns:** `str` - Less saturated hex color

**Example:**

```python
less_saturated = vg.desaturate("#3498db", 0.3)  # Returns: '#4683c0'
```

---

### shift_hue()

**Function:** `shift_hue(color, degrees)`

Rotate the hue of a color by a specified number of degrees on the color wheel.

**Parameters:**
- `color` (str): Hex color string
- `degrees` (float): Degrees to rotate, can be negative or positive (-360 to 360)

**Returns:** `str` - Color with shifted hue

**Example:**

```python
# Rotate red 120 degrees to get green
shifted = vg.shift_hue("#FF0000", 120)  # Returns: '#00ff00'

# Negative rotation
shifted = vg.shift_hue("#FF0000", -120)  # Returns: '#0000ff'
```

---

### invert()

**Function:** `invert(color)`

Invert a color by flipping its RGB values.

**Parameters:**
- `color` (str): Hex color string

**Returns:** `str` - Inverted hex color

**Example:**

```python
inverted = vg.invert("#FF0000")  # Returns: '#00ffff' (Red → Cyan)
inverted = vg.invert("#3498db")  # Returns: '#cb6724'
```

---

### mix()

**Function:** `mix(color1, color2, weight=0.5)`

Mix two colors together with a specified weight.

**Parameters:**
- `color1` (str): First hex color
- `color2` (str): Second hex color
- `weight` (float): Weight of first color between 0 and 1 (default: `0.5` for 50/50 mix)

**Returns:** `str` - Mixed hex color

**Example:**

```python
# Equal mix (50/50)
mixed = vg.mix("#FF0000", "#0000FF", 0.5)  # Returns: '#7f007f' (Purple)

# More of the first color (80% red, 20% blue)
mixed = vg.mix("#FF0000", "#0000FF", 0.8)  # Returns: '#cc0033'

# More of the second color (20% red, 80% blue)
mixed = vg.mix("#FF0000", "#0000FF", 0.2)  # Returns: '#3300cc'
```

---

## Accessibility Functions

### calculate_contrast_ratio()

**Function:** `calculate_contrast_ratio(color1, color2)`

Calculate WCAG 2.1 contrast ratio between two colors.

**Parameters:**
- `color1` (str): First hex color
- `color2` (str): Second hex color

**Returns:** `float` - Contrast ratio (1-21, where 21 is maximum contrast)

**Example:**

```python
ratio = vg.calculate_contrast_ratio("#FFFFFF", "#000000")  # 21.0
ratio = vg.calculate_contrast_ratio("#3498db", "#1a1a1a")  # ~5.2
```

---

### meets_wcag()

**Function:** `meets_wcag(color1, color2, level="AA", large_text=False)`

Check if two colors meet WCAG contrast requirements.

**Parameters:**
- `color1` (str): Foreground hex color
- `color2` (str): Background hex color
- `level` (str): WCAG conformance level - `"AA"` or `"AAA"` (default: `"AA"`)
- `large_text` (bool): `True` if text is 18pt+ or 14pt+ bold (default: `False`)

**Returns:** `bool` - `True` if colors meet the specified WCAG level

**WCAG Requirements:**
- **AA Normal Text:** 4.5:1 minimum
- **AA Large Text:** 3:1 minimum
- **AAA Normal Text:** 7:1 minimum
- **AAA Large Text:** 4.5:1 minimum

**Example:**

```python
if vg.meets_wcag("#FFFFFF", "#000000", "AAA"):
    print("Perfect contrast!")

if not vg.meets_wcag("#777777", "#888888", "AA"):
    print("Insufficient contrast for normal text")
```

---

### ensure_contrast()

**Function:** `ensure_contrast(foreground, background, min_ratio=4.5, max_iterations=20)`

Automatically adjust a foreground color to meet minimum contrast requirements against a background.

**Parameters:**
- `foreground` (str): Foreground hex color to adjust
- `background` (str): Background hex color (not modified)
- `min_ratio` (float): Minimum contrast ratio to achieve (default: `4.5`)
- `max_iterations` (int): Maximum adjustment attempts (default: `20`)

**Returns:** `str` - Adjusted hex color that meets contrast requirement

**Example:**

```python
# Ensure text is readable on gray background
adjusted = vg.ensure_contrast("#888888", "#999999", min_ratio=4.5)
# Returns darkened/lightened color that meets contrast requirement
```

---

## Color Blindness Functions

### simulate_colorblindness()

**Function:** `simulate_colorblindness(hex_color, cb_type)`

Simulate how a color appears to individuals with various types of color blindness.

**Parameters:**
- `hex_color` (str): Input hex color
- `cb_type` (str): Type of color blindness to simulate

**Color Blindness Types:**
- `"protanopia"` - Red-blind (no red cones)
- `"deuteranopia"` - Green-blind (no green cones)
- `"tritanopia"` - Blue-blind (no blue cones)
- `"protanomaly"` - Red-weak (defective red cones)
- `"deuteranomaly"` - Green-weak (defective green cones)
- `"tritanomaly"` - Blue-weak (defective blue cones)

**Returns:** `str` - Hex color as perceived by someone with the specified color blindness

**Example:**

```python
# How red appears to someone with deuteranopia
simulated = vg.simulate_colorblindness("#FF0000", "deuteranopia")
# Returns: '#b89000' (brownish-yellow)

# Test all your colors
for color in palette:
    sim = vg.simulate_colorblindness(color, "deuteranopia")
    print(f"{color} → {sim}")
```

---

### validate_colorblind_safety()

**Function:** `validate_colorblind_safety(colors, cb_type="deuteranopia", min_difference=30)`

Check if colors in a palette remain distinguishable for people with color blindness.

**Parameters:**
- `colors` (list): List of hex color strings
- `cb_type` (str): Type of color blindness to test (default: `"deuteranopia"`)
- `min_difference` (float): Minimum perceptual difference required (default: `30`)

**Returns:** `tuple` - `(is_safe: bool, problems: list)` where problems is a list of `(index, index)` tuples indicating indistinguishable color pairs

**Example:**

```python
colors = ["#FF0000", "#00FF00", "#0000FF"]
is_safe, problems = vg.validate_colorblind_safety(colors, "deuteranopia")

if not is_safe:
    for i, j in problems:
        print(f"Colors {i} and {j} are too similar: {colors[i]} vs {colors[j]}")
```

---

## Persistence Functions

### save_palette()

**Function:** `save_palette(colors, filename, metadata=None)`

Save a color palette to a JSON file for later use.

**Parameters:**
- `colors` (list): List of hex color strings
- `filename` (str): Output file path
- `metadata` (dict, optional): Optional metadata dictionary to include

**Returns:** `None`

**Example:**

```python
palette = vg.generate_palette("#3498db", "complementary", 5)
vg.save_palette(
    palette,
    "my_theme.json",
    metadata={"name": "Ocean Blue", "scheme": "complementary"}
)
```

---

### load_palette()

**Function:** `load_palette(filename)`

Load a color palette from a JSON file.

**Parameters:**
- `filename` (str): Input file path

**Returns:** `tuple` - `(colors: list, metadata: dict)` containing the color list and metadata

**Example:**

```python
colors, metadata = vg.load_palette("my_theme.json")
print(f"Loaded: {metadata['name']}")
print(vg.preview_palette(colors))
```

---

### save_theme()

**Function:** `save_theme(theme, filename, metadata=None)`

Save a theme palette to a JSON file.

**Parameters:**
- `theme` (dict): Theme dictionary from `generate_theme_palette()`
- `filename` (str): Output file path
- `metadata` (dict, optional): Optional metadata dictionary to include

**Returns:** `None`

**Example:**

```python
theme = vg.generate_theme_palette("triadic", "#9b59b6")
vg.save_theme(
    theme,
    "purple_theme.json",
    metadata={"name": "Purple Rain", "author": "Me"}
)
```

---

### load_theme()

**Function:** `load_theme(filename)`

Load a theme palette from a JSON file.

**Parameters:**
- `filename` (str): Input file path

**Returns:** `tuple` - `(theme: dict, metadata: dict)` containing the theme dictionary and metadata

**Example:**

```python
theme, metadata = vg.load_theme("purple_theme.json")
vg.apply_palette_theme(theme)
print(vg.format("<primary>Using loaded theme!</primary>"))