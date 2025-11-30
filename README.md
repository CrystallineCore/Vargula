
<h1>
  Vargula
  <span style="float:right;">
    <a href="https://github.com/CrystallineCore/Vargula">
      <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
    </a>
    <a href="https://pypi.org/project/vargula/">
      <img src="https://img.shields.io/badge/pypi-%23ececec.svg?style=for-the-badge&logo=pypi&logoColor=1f73b7">
    </a>
    <a href="https://vargula.readthedocs.io/">
      <img src="https://img.shields.io/badge/Read%20the%20Docs-%23000000?style=for-the-badge&logo=readthedocs&logoColor=white">
    </a>
  </span>
</h1>


[![PyPI Downloads](https://static.pepy.tech/personalized-badge/vargula?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/vargula)
![PyPI - Version](https://img.shields.io/pypi/v/vargula)
[![Documentation Status](https://readthedocs.org/projects/vargula/badge/?version=latest)](https://vargula.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)





**Simple cross-platform terminal text styling library with advanced color palette generation**

Vargula is a powerful Python library for terminal styling that combines better functionality with comprehensive color theory tools. Style your terminal output with colors, create beautiful tables, show progress bars, and generate harmonious color palettes - all with a simple, intuitive API.

Try [this](https://pastebin.com/BpGDZkfu) Vargula's code snippet to run this:

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-46-17.gif?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-46-17.gif?raw=true)

## What's new?

### BREAKING CHANGES
- **API Restructured to Class-Based Design**: Major refactoring for better organization and thread-safety
  - All functionality now accessed through `Vargula` class instances
  - Removed module-level global functions (global state eliminated)
  - Each instance maintains independent state for thread-safe operations

Refer the *API Reference* section to know more.

##  Features

-  **Text Styling**: Colors, backgrounds, and text decorations (bold, italic, underline, etc.)
-  **Markup Syntax**: HTML-like tags for inline styling (`<red>error</red>`)
-  **Tables**: Rich-style tables with customizable borders and styling
-  **Progress Bars**: Customizable progress indicators with ETA and rate display
-  **Color Palettes**: Generate harmonious color schemes based on color theory
-  **Accessibility**: WCAG contrast checking and colorblind simulation
-  **Themes**: Built-in themes and custom theme support
-  **Cross-platform**: Works on Windows, macOS, and Linux

##

##  Installation

```bash
pip install vargula
```
Or clone from Github repository: [Vargula](https://github.com/crystallinecore/vargula)

##

## Quick Start

```python
from vargula import Vargula

vg = Vargula()

vg.create("added", color="#00ff88", bg="#003322")
vg.create("removed", color="#ff4444", bg="#330000")
vg.create("modified", color="#ffaa00", bg="#332200")

diff_lines = [
("  ", "def calculate_total(items):"),
("-", "    total = 0"),
("+", "    total = Decimal('0.00')"),
("  ", "    for item in items:"),
("-", "        total += item.price"),
("+", "        total += Decimal(str(item.price))"),
("  ", "    return total"),
]

for marker, line in diff_lines:
    if marker == "+":
        print(vg.format(f"<added>{marker} {line}</added>"))
    elif marker == "-":
        print(vg.format(f"<removed>{marker} {line}</removed>"))
    else:
        print(f"{marker} {line}")
```

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-41-22.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-41-22.png?raw=true)

##

## Tag Syntax Conventions

Vargula supports inline color styling using intuitive tag syntax:

- **`<#hexcode>`** - Set foreground (text) color using hex codes
- **`<@#hexcode>`** - Set background color using hex codes
- **`<colorname>`** - Apply named foreground color (e.g., `red`, `blue`, `bright_green`)
- **`<@colorname>`** - Apply named background color (e.g., `<@red>`, `<@yellow>`)
- **`<lookname>`** - Apply text style (e.g., `bold`, `italic`, `underline`)
- **`<customname>`** - Apply custom styles created with `create()`
- **`\\<tag>`** - Ignores the tag and prints as is. 
- **`\<tag>`** - Ignores the tag and prints as is, if used as a raw string. (i.e. `r"\<tag>"`) 

### Examples

```py
from vargula import Vargula
vg = Vargula()

# Named foreground colors
vg.write("<red>Red text</red>")
vg.write("<bright_blue>Bright blue text</bright_blue>")

# Named background colors
vg.write("<@yellow>Yellow background</@yellow>")
vg.write("<@red>Red background</@red>")
vg.write("<@bright_black>Dark background</@bright_black>")

# Hex foreground color
vg.write("<#FF5733>Orange text</#FF5733>")
vg.write("<#3498db>Blue text</#3498db>")

# Hex background color
vg.write("<@#FF0000>Red background</@#FF0000>")
vg.write("<@#F00>Short hex red background</@#F00>")

# Foreground + background combination
vg.write("<#FFFFFF><@#000000>White text on black</@#000000></#FFFFFF>")
vg.write("<green><@black>Green on black</@black></green>")

# Mix with text styles
vg.write("<bold><#00FF00><@#000080>Bold green on navy</@#000080></#00FF00></bold>")
vg.write("<italic><@yellow>Italic on yellow</@yellow></italic>")

# Nested backgrounds
vg.write("<@yellow>Yellow <@red>then red</@red> back to yellow</@yellow>")
vg.write("<@#FF0000>Hex red <@yellow>named yellow</@yellow> back to hex</@#FF0000>")

# Complex nesting
vg.write("<bold><red>Bold <italic>and italic</italic> red text</red></bold>")

#Escape sequences
vg.write(r"Use \<red>text\</red> to make text red")
vg.create("syntax", color="yellow")
vg.write(r"Tag syntax: \<syntax>highlighted code\</syntax> becomes <syntax>highlighted code</syntax>")
```

**Output:**

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-24%2017-30-24.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-24%2017-30-24.png?raw=true)

### Tag Format Rules

- **Hex codes** can be 3 or 6 characters: `<#F00>` or `<#FF0000>`
- **The `#` prefix** is for foreground hex colors: `<#FF5733>`
- **The `@` prefix** is required for all background colors (named or hex): `<@yellow>`, `<@FF0000>`
- **Tags are case-insensitive** for named colors: `<red>` and `<RED>` work the same
- **Closing tags** must match opening tags exactly: `<@yellow>...</@yellow>`
- **Tags can be nested** arbitrarily deep for complex styling
- **Use `\` or `\\`** for escaping sequences

### Available Named Colors

**Standard colors:** `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`

**Bright variants:** `bright_black`, `bright_red`, `bright_green`, `bright_yellow`, `bright_blue`, `bright_magenta`, `bright_cyan`, `bright_white`

**Text styles:** `bold`, `dim`, `italic`, `underline`, `blink`, `reverse`, `hidden`, `strikethrough`

##

## API Reference
### Creating Instances

#### Instance-Based API (Recommended for Applications)

For applications requiring multiple themes, thread-safety, or isolated state, create custom `Vargula` instances:
```python
from vargula import Vargula

# Create independent instances
vg_dark = Vargula()
vg_light = Vargula()

# Create custom styles per instance
vg_dark.create("error", color="bright_red", look="bold")
vg_light.create("error", color="cyan", look="underline")

# Use independently without interference
vg_dark.write("<error>Error in theme one</error>")
vg_light.write("<error>Error in theme two</error>")
```
**Output:**

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-30%2015-43-47.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-30%2015-43-47.png?raw=true)

**Benefits of instance-based approach:**
- Each instance has completely isolated state (styles, themes, settings)
- Multiple themes can coexist in the same application
- Perfect for multi-component applications
- Enables true thread-safe operations

#### Thread-Safe Operations

Each `Vargula` instance maintains its own state, making them inherently thread-safe when used independently. This is essential for concurrent applications:
```python
from vargula import Vargula
import threading
import time

def process_with_theme(theme_name: str, task_id: int):
    """Each thread creates its own instance for complete isolation"""
    # Create a dedicated instance for this thread
    vg = Vargula()
    vg.set_theme(theme_name)
    
    # Do work with isolated styling
    for i in range(3):
        vg.write(f"[Task {task_id}] Step {i+1} processing...")
        time.sleep(0.5)
    
    vg.write(f"[Task {task_id}] <green>Complete!</green>")

# Create threads with different themes
threads = [
    threading.Thread(target=process_with_theme, args=("dark", 1)),
    threading.Thread(target=process_with_theme, args=("light", 2)),
    threading.Thread(target=process_with_theme, args=("dark", 3))
]

# Start all threads - no style interference between them
for thread in threads:
    thread.start()

# Wait for completion
for thread in threads:
    thread.join()
```
**Output:**

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-30%2015-36-01.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-30%2015-36-01.png?raw=true)

**Why this matters for threading:**
- No global state to cause race conditions
- Each thread can have its own theme
- Styles set in one thread don't affect others
- Safe for use in thread pools and async contexts



### Core Styling Functions
#### `style(text, color=None, bg=None, look=None)`

Apply styling to text directly.

**Parameters:**
- `text` (str): Text to style
- `color` (str|tuple): Foreground color (name, hex, or RGB tuple)
- `bg` (str|tuple): Background color (name, hex, or RGB tuple)
- `look` (str|list): Text decoration(s) - "bold", "italic", "underline", etc.

**Returns:** Styled string with ANSI codes

**Examples:**
```python
# Named colors
print(vg.style("Error", color="red", look="bold"))

# Hex colors
print(vg.style("Custom", color="#FF5733", bg="#1a1a1a"))

# RGB tuples
print(vg.style("RGB", color=(255, 87, 51)))

# Multiple looks
print(vg.style("Fancy", color="cyan", look=["bold", "underline"]))
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-43-36.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-43-36.png?raw=true)


**Available Colors:**
- Basic: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`
- Bright: `bright_black`, `bright_red`, `bright_green`, `bright_yellow`, `bright_blue`, `bright_magenta`, `bright_cyan`, `bright_white`

**Available Looks:**
- `bold`, `dim`, `italic`, `underline`, `blink`, `reverse`, `hidden`, `strikethrough`



##

#### `format(text)`

Format text using HTML-like markup tags.

**Parameters:**
- `text` (str): Text with markup tags

**Returns:** Formatted string with ANSI codes

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

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-46-26.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-46-26.png?raw=true)

##

#### `create(name, color=None, bg=None, look=None)`

Create a custom reusable style tag.

**Parameters:**
- `name` (str): Name of the custom style
- `color` (str|tuple): Foreground color
- `bg` (str|tuple): Background color
- `look` (str|list): Text decoration(s)

**Returns:** None

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

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-48-45.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-48-45.png?raw=true)


##

#### `delete(name)`

Delete a custom style tag.

**Parameters:**
- `name` (str): Name of the style to delete

**Returns:** bool - True if deleted, False if not found

**Example:**
```python
vg.create("temp", color="blue")
vg.delete("temp")  # Returns True
vg.delete("temp")  # Returns False (already deleted)
```

##

#### `write(*args, sep=" ", end="\n", file=None, flush=False)`

Format and print text with markup in one call. Works exactly like built-in `print()` but automatically formats markup tags.

**Parameters:**
- `*args`: Values to print (will be converted to strings and formatted)
- `sep` (str): String inserted between values (default: single space)
- `end` (str): String appended after the last value (default: newline)
- `file`: File object; defaults to sys.stdout
- `flush` (bool): Whether to forcibly flush the stream

**Returns:** None (prints to stdout)

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
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2016-35-49.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2016-35-49.png?raw=true)

##

#### `strip(text)`

Remove all markup tags from text.

**Parameters:**
- `text` (str): Text containing markup tags

**Returns:** Plain text without tags

**Example:**
```python
text = "Hello <red>world</red>!"
plain = vg.strip(text)  # "Hello world!"
```

##

#### `clean(text)`

Remove all ANSI escape codes from text.

**Parameters:**
- `text` (str): Text containing ANSI codes

**Returns:** Plain text without ANSI codes

**Example:**
```python
styled = vg.style("Colored", color="red")
plain = vg.clean(styled)  # "Colored" (no ANSI codes)
```

##

#### `length(text)`

Calculate visible length of text (ignoring ANSI codes).

**Parameters:**
- `text` (str): Text with ANSI codes

**Returns:** int - Visible character count

**Example:**
```python
styled = vg.style("Hello", color="red")
print(len(styled))        # 18 (includes ANSI codes)
print(vg.length(styled))  # 5 (visible length)
```

##

#### `enable()` / `disable()`

Globally enable or disable styling.

**Parameters:** None

**Returns:** None

**Example:**
```python
vg.disable()
print(vg.style("No color", color="red"))  # Prints plain text

vg.enable()
print(vg.style("Has color", color="red"))  # Prints colored text
```

##

#### `temporary(name, color=None, bg=None, look=None)`

Context manager for temporary custom styles.

**Parameters:** Same as `create()`

**Returns:** Context manager

**Example:**
```python
with vg.temporary("temp", color="cyan", look="bold"):
    print(vg.format("<temp>Temporary style</temp>"))
# "temp" style is automatically deleted after the block
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-51-49.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-51-49.png?raw=true)

##

### Theme Functions

#### `set_theme(theme)`

Set a predefined or custom theme.

**Parameters:**
- `theme` (str|dict): Theme name ("dark", "light") or custom theme dictionary

**Returns:** None

**Example:**
```python
# Built-in themes
vg.set_theme("dark")
print(vg.format("<error>Error!</error> <success>OK</success>"))

vg.set_theme("light")
print(vg.format("<warning>Warning</warning>"))

# Custom theme
custom = {
    "error": {"color": "red", "look": "bold"},
    "info": {"color": "blue"},
    "highlight": {"bg": "yellow", "color": "black"}
}
vg.set_theme(custom)
```

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-53-57.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-53-57.png?raw=true)

**Built-in Theme Styles:**
- `error`, `success`, `warning`, `info`, `debug`, `critical`

##

###  Tables

#### `Table(title=None, caption=None, ...)`

Create a Rich-style table with customizable styling.

**Parameters:**
- `title` (str): Optional title above table
- `caption` (str): Optional caption below table
- `style` (str): Default style for all cells
- `title_style` (str): Style for title (default: "bold")
- `caption_style` (str): Style for caption (default: "dim")
- `header_style` (str): Style for header row (default: "bold")
- `border_style` (str): Style for border characters
- `show_header` (bool): Show header row (default: True)
- `show_lines` (bool): Show lines between rows (default: False)
- `padding` (tuple): (vertical, horizontal) padding (default: (0, 1))
- `expand` (bool): Expand to full terminal width (default: False)
- `min_width` (int): Minimum table width
- `box` (str): Border style (default: "rounded")

**Box Styles:**
- `"rounded"` - Rounded corners (╭─╮)
- `"square"` - Square corners (┌─┐)
- `"double"` - Double lines (╔═╗)
- `"heavy"` - Heavy lines (┏━┓)
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

**Output:**

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-54-28.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-54-28.png?raw=true)
##

#### `Table.add_column(header, style=None, justify="left", ...)`

Add a column to the table.

**Parameters:**
- `header` (str): Column header text
- `style` (str): Style for this column's cells
- `justify` (str): Alignment - "left", "center", "right"
- `no_wrap` (bool): Disable text wrapping
- `overflow` (str): Overflow handling - "ellipsis", "crop", "fold"
- `width` (int): Fixed column width
- `min_width` (int): Minimum column width
- `max_width` (int): Maximum column width

**Example:**
```python
table.add_column("Name", style="bold", justify="left", width=20)
table.add_column("Score", style="green", justify="right", max_width=10)
table.add_column("Status", justify="center")
```

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-54-47.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-54-47.png?raw=true)

##

#### `Table.add_row(*cells, style=None)`

Add a row of data to the table.

**Parameters:**
- `*cells`: Cell values (one per column)
- `style` (str): Style for entire row (overrides column styles)

**Example:**
```python
table.add_row("Alice", "95", "Active")
table.add_row("Bob", "87", "Active", style="dim")  # Dimmed row
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-55-08.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2007-55-08.png?raw=true)
##

### Progress Bars

#### `ProgressBar(total=100, desc="", ...)`

Create a customizable progress bar.

**Parameters:**
- `total` (int): Total number of iterations
- `desc` (str): Description text
- `unit` (str): Unit name (e.g., "files", "items", "it")
- `bar_width` (int): Width of progress bar (default: 40)
- `complete_style` (str): Style for completed portion (default: "green")
- `incomplete_style` (str): Style for incomplete portion (default: "bright_black")
- `percentage_style` (str): Style for percentage (default: "cyan")
- `desc_style` (str): Style for description (default: "bold")
- `show_percentage` (bool): Show percentage (default: True)
- `show_count` (bool): Show count (default: True)
- `show_rate` (bool): Show processing rate (default: True)
- `show_eta` (bool): Show estimated time (default: True)
- `refresh_rate` (float): Min seconds between updates (default: 0.1)

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

**Output:**

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2007-57-51.gif?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2007-57-51.gif?raw=true)


##

#### `ProgressBar.update(n=1)`

Update progress by n steps.

**Parameters:**
- `n` (int): Number of steps to advance (default: 1)

**Example:**
```python
pbar = vg.ProgressBar(total=100)
pbar.update(1)   # Advance by 1
pbar.update(10)  # Advance by 10
```

##

#### `ProgressBar.close()`

Complete and close the progress bar.

**Example:**
```python
pbar = vg.ProgressBar(total=100)
# ... work ...
pbar.close()  # Ensures final state is displayed
```

##

#### `progress_bar(iterable, total=None, desc="", **kwargs)`

Wrap an iterable with a progress bar.

**Parameters:**
- `iterable`: Any iterable object
- `total` (int): Total count (auto-detected if possible)
- `desc` (str): Description
- `**kwargs`: Additional ProgressBar arguments

**Returns:** Iterator yielding items from iterable

**Example:**
```python
import time

for item in vg.progress_bar(range(100), desc="Processing"):
    # Process item
    time.sleep(0.01)
```

**Output:**

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-00-53.gif?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-00-53.gif?raw=true)

##

#### `MultiProgress()`

Manage multiple progress bars simultaneously.

**Example:**
```python
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

**Output:**

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-03-51.gif?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-03-51.gif?raw=true)

##

#### `MultiProgress.add_task(desc, total=100, **kwargs)`

Add a new progress task.

**Parameters:**
- `desc` (str): Task description
- `total` (int): Total iterations
- `**kwargs`: Additional ProgressBar arguments

**Returns:** int - Task ID for updating

##

#### `MultiProgress.update(task_id, n=1)`

Update a specific task.

**Parameters:**
- `task_id` (int): ID returned from add_task()
- `n` (int): Steps to advance

##

###  Color Palette Generation

#### `generate_palette(base_color=None, scheme="random", count=5, ...)`

Generate a color palette based on color theory.

**Parameters:**
- `base_color` (str): Starting hex color (e.g., '#FF5733'). Random if None
- `scheme` (str): Color harmony scheme
- `count` (int): Number of colors to generate
- `saturation_range` (tuple): (min, max) saturation (0-1)
- `value_range` (tuple): (min, max) brightness (0-1)
- `randomize` (bool): Add slight variations (default: True)

**Returns:** List of hex color strings

**Schemes:**
- `"monochromatic"` - Single hue variations
- `"analogous"` - Adjacent hues (±30°)
- `"complementary"` - Opposite hues (180°)
- `"triadic"` - Three evenly spaced hues (120°)
- `"tetradic"` - Four hues (60°, 180°, 240°)
- `"split_complementary"` - Base + two adjacent to complement
- `"square"` - Four evenly spaced hues (90°)
- `"random"` - Random colors

**Examples:**
```python
# Complementary palette from blue
colors = vg.generate_palette("#3498db", "complementary", 5)
# ['#3498db', '#db7834', '#34a4db', '#db3449', '#4ddb34']

# Random palette
colors = vg.generate_palette(scheme="random", count=8)

# Analogous with custom ranges
colors = vg.generate_palette(
    base_color="#e74c3c",
    scheme="analogous",
    count=6,
    saturation_range=(0.6, 0.9),
    value_range=(0.6, 0.95)
)
```

##

#### `generate_theme_palette(scheme="random", base_color=None, ...)`

Generate a complete theme with semantic colors.

**Parameters:**
- `scheme` (str): Color harmony scheme
- `base_color` (str): Optional base color
- `include_neutrals` (bool): Add grayscale colors (default: True)
- `force_semantic_colors` (bool): Use standard colors for success/warning/error (default: False)

**Returns:** Dictionary mapping theme names to hex colors

**Example:**
```python
theme = vg.generate_theme_palette("complementary", "#3498db")
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

##

#### `generate_accessible_theme(base_color, scheme="complementary", ...)`

Generate theme with WCAG contrast validation.

**Parameters:**
- `base_color` (str): Base hex color
- `scheme` (str): Color harmony scheme
- `background` (str): Background color (default: "#1a1a1a")
- `min_contrast` (float): Minimum contrast ratio (default: 4.5)
- `wcag_level` (str): "AA" or "AAA"

**Returns:** Dictionary with accessible colors

**Example:**
```python
# All colors will meet WCAG AA on white background
theme = vg.generate_accessible_theme(
    "#3498db",
    scheme="triadic",
    background="#ffffff",
    wcag_level="AA"
)
```

##

#### `preview_palette(colors, width=40, show_info=True)`

Generate text preview of a color palette.

**Parameters:**
- `colors` (list): List of hex colors
- `width` (int): Width of color blocks (default: 40)
- `show_info` (bool): Show HSV values (default: True)

**Returns:** Formatted string with colored blocks

**Example:**
```python
colors = vg.generate_palette("#3498db", "analogous", 5)
print(vg.preview_palette(colors))
```

**Output:**

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-06-53.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-06-53.png?raw=true)

##

#### `apply_palette_theme(palette, register_styles=True)`

Apply a generated palette as the active theme.

**Parameters:**
- `palette` (dict): Dictionary from generate_theme_palette()
- `register_styles` (bool): Register each color as custom style (default: True)

**Example:**
```python
theme = vg.generate_theme_palette("analogous", "#e74c3c")
vg.apply_palette_theme(theme)

print(vg.format("<primary>Primary</primary>"))
print(vg.format("<success>Success</success>"))
print(vg.format("<error>Error</error>"))
```

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-07-44.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-07-44.png?raw=true)
##

###  Color Manipulation

#### `lighten(color, amount=0.1)`

Increase brightness of a color.

**Parameters:**
- `color` (str): Hex color
- `amount` (float): Brightness increase (0-1)

**Returns:** Hex color string

**Example:**
```python
lighter = vg.lighten("#3498db", 0.2)  # '#3cb0ff'
```

##

#### `darken(color, amount=0.1)`

Decrease brightness of a color.

**Parameters:**
- `color` (str): Hex color
- `amount` (float): Brightness decrease (0-1)

**Returns:** Hex color string

**Example:**
```python
darker = vg.darken("#3498db", 0.2)  # '#2774a7'
```

##

#### `saturate(color, amount=0.1)`

Increase saturation of a color.

**Parameters:**
- `color` (str): Hex color
- `amount` (float): Saturation increase (0-1)

**Returns:** Hex color string

**Example:**
```python
more_saturated = vg.saturate("#80a0c0", 0.3)  # '#5a9ad8'
```

##

#### `desaturate(color, amount=0.1)`

Decrease saturation of a color.

**Parameters:**
- `color` (str): Hex color
- `amount` (float): Saturation decrease (0-1)

**Returns:** Hex color string

**Example:**
```python
less_saturated = vg.desaturate("#3498db", 0.3)  # '#4683c0'
```

##

#### `shift_hue(color, degrees)`

Rotate hue by specified degrees.

**Parameters:**
- `color` (str): Hex color
- `degrees` (float): Degrees to rotate (-360 to 360)

**Returns:** Hex color string

**Example:**
```python
shifted = vg.shift_hue("#FF0000", 120)  # '#00ff00' (Red → Green)
```

##

#### `invert(color)`

Invert a color.

**Parameters:**
- `color` (str): Hex color

**Returns:** Hex color string

**Example:**
```python
inverted = vg.invert("#FF0000")  # '#00ffff' (Red → Cyan)
```

##

#### `mix(color1, color2, weight=0.5)`

Mix two colors together.

**Parameters:**
- `color1` (str): First hex color
- `color2` (str): Second hex color
- `weight` (float): Weight of first color (0-1, default: 0.5)

**Returns:** Hex color string

**Example:**
```python
mixed = vg.mix("#FF0000", "#0000FF", 0.5)  # '#7f007f' (Purple)
mixed = vg.mix("#FF0000", "#0000FF", 0.8)  # More red
```

##

###  Accessibility Functions

#### `calculate_contrast_ratio(color1, color2)`

Calculate WCAG 2.1 contrast ratio.

**Parameters:**
- `color1` (str): First hex color
- `color2` (str): Second hex color

**Returns:** float - Contrast ratio (1-21, 21 is max)

**Example:**
```python
ratio = vg.calculate_contrast_ratio("#FFFFFF", "#000000")  # 21.0
ratio = vg.calculate_contrast_ratio("#3498db", "#1a1a1a")  # ~5.2
```

##

#### `meets_wcag(color1, color2, level="AA", large_text=False)`

Check if colors meet WCAG contrast requirements.

**Parameters:**
- `color1` (str): Foreground hex color
- `color2` (str): Background hex color
- `level` (str): "AA" or "AAA"
- `large_text` (bool): True if text is 18pt+ or 14pt+ bold

**Returns:** bool

**WCAG Requirements:**
- **AA Normal Text**: 4.5:1 minimum
- **AA Large Text**: 3:1 minimum
- **AAA Normal Text**: 7:1 minimum
- **AAA Large Text**: 4.5:1 minimum

**Example:**
```python
if vg.meets_wcag("#FFFFFF", "#000000", "AAA"):
    print("Perfect contrast!")

if not vg.meets_wcag("#777777", "#888888", "AA"):
    print("Insufficient contrast for normal text")
```

##

#### `ensure_contrast(foreground, background, min_ratio=4.5, max_iterations=20)`

Adjust foreground color to meet minimum contrast.

**Parameters:**
- `foreground` (str): Foreground hex color to adjust
- `background` (str): Background hex color
- `min_ratio` (float): Minimum contrast ratio (default: 4.5)
- `max_iterations` (int): Max adjustment attempts (default: 20)

**Returns:** Adjusted hex color

**Example:**
```python
# Ensure text is readable on gray background
adjusted = vg.ensure_contrast("#888888", "#999999", min_ratio=4.5)
# Returns darkened/lightened color that meets contrast requirement
```

##

###  Color Blindness Functions

#### `simulate_colorblindness(hex_color, cb_type)`

Simulate how a color appears to colorblind individuals.

**Parameters:**
- `hex_color` (str): Input hex color
- `cb_type` (str): Type of color blindness

**Types:**
- `"protanopia"` - Red-blind (no red cones)
- `"deuteranopia"` - Green-blind (no green cones)
- `"tritanopia"` - Blue-blind (no blue cones)
- `"protanomaly"` - Red-weak (defective red cones)
- `"deuteranomaly"` - Green-weak (defective green cones)
- `"tritanomaly"` - Blue-weak (defective blue cones)

**Returns:** Hex color as seen by colorblind person

**Example:**
```python
# How red appears to someone with deuteranopia
simulated = vg.simulate_colorblindness("#FF0000", "deuteranopia")
# '#b89000' (brownish-yellow)

# Test all your colors
for color in palette:
    sim = vg.simulate_colorblindness(color, "deuteranopia")
    print(f"{color} → {sim}")
```

##

#### `validate_colorblind_safety(colors, cb_type="deuteranopia", min_difference=30)`

Check if palette colors are distinguishable.

**Parameters:**
- `colors` (list): List of hex colors
- `cb_type` (str): Color blindness type
- `min_difference` (float): Min perceptual difference (default: 30)

**Returns:** Tuple of (is_safe: bool, problems: list of (index, index) tuples)

**Example:**
```python
colors = ["#FF0000", "#00FF00", "#0000FF"]
is_safe, problems = vg.validate_colorblind_safety(colors, "deuteranopia")

if not is_safe:
    for i, j in problems:
        print(f"Colors {i} and {j} are too similar: {colors[i]} vs {colors[j]}")
```

##

### Persistence Functions

#### `save_palette(colors, filename, metadata=None)`

Save color palette to JSON file.

**Parameters:**
- `colors` (list): List of hex colors
- `filename` (str): Output file path
- `metadata` (dict): Optional metadata

**Example:**
```python
palette = vg.generate_palette("#3498db", "complementary", 5)
vg.save_palette(
    palette,
    "my_theme.json",
    metadata={"name": "Ocean Blue", "scheme": "complementary"}
)
```

##

#### `load_palette(filename)`

Load color palette from JSON file.

**Parameters:**
- `filename` (str): Input file path

**Returns:** Tuple of (colors: list, metadata: dict)

**Example:**
```python
colors, metadata = vg.load_palette("my_theme.json")
print(f"Loaded: {metadata['name']}")
print(vg.preview_palette(colors))
```

##

#### `save_theme(theme, filename, metadata=None)`

Save theme palette to JSON file.

**Parameters:**
- `theme` (dict): Theme from generate_theme_palette()
- `filename` (str): Output file path
- `metadata` (dict): Optional metadata

**Example:**
```python
theme = vg.generate_theme_palette("triadic", "#9b59b6")
vg.save_theme(
    theme,
    "purple_theme.json",
    metadata={"name": "Purple Rain", "author": "Me"}
)
```

##

#### `load_theme(filename)`

Load theme palette from JSON file.

**Parameters:**
- `filename` (str): Input file path

**Returns:** Tuple of (theme: dict, metadata: dict)

**Example:**
```python
theme, metadata = vg.load_theme("purple_theme.json")
vg.apply_palette_theme(theme)
print(vg.format("<primary>Using loaded theme!</primary>"))
```

##

## Complete Examples

### Example 1: Color Palette Explorer

```python
import vargula

vg = vargula.Vargula()

# Generate and preview different color schemes
schemes = ["analogous", "complementary", "triadic", "tetradic"]

for scheme in schemes:
    print(vg.format(f"\n<bold><cyan>{scheme.upper()} Palette</cyan></bold>"))
    palette = vg.generate_palette("#3498db", scheme, count=6)
    print(vg.preview_palette(palette, width=30))
    
    # Check accessibility
    is_safe, problems = vg.validate_colorblind_safety(palette)
    if is_safe:
        print(vg.format("<green>✓ Colorblind-safe</green>"))
    else:
        print(vg.format(f"<yellow>⚠ {len(problems)} similar color pairs</yellow>"))
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-09-58.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-09-58.png?raw=true)

##

### Example 2: Themed CLI Application

```python
import vargula
import time

vg = vargula.Vargula()

# Generate and apply theme
theme = vg.generate_theme_palette("analogous", "#e74c3c")
vg.apply_palette_theme(theme)

# Create custom log styles
vg.create("timestamp", color="#666666")
vg.create("user", color="cyan", look="bold")

# Styled output
vg.write("<timestamp>[12:34:56]</timestamp> <user>admin</user> logged in")
vg.write("<success>✓ Database connection established</success>")
vg.write("<warning>⚠ Cache expiring soon</warning>")
vg.write("<error>✗ Failed to connect to API</error>")

# Progress with theme colors
with vg.ProgressBar(
    total=100,
    desc="Syncing",
    complete_style="primary",
    percentage_style="accent"
) as pbar:
    for i in range(100):
        pbar.update(1)
        time.sleep(0.02)
```

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/update.gif?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/update.gif?raw=true)

##

### Example 3: Accessible Theme Generator

```python
import vargula

vg = vargula.Vargula()

# Generate accessible theme for light background
theme = vg.generate_accessible_theme(
    base_color="#3498db",
    scheme="complementary",
    background="#ffffff",
    wcag_level="AAA"
)

# Verify contrast ratios
vg.write("<bold>Theme Accessibility Report</bold>\n")

for name, color in theme.items():
    if name in ["primary", "secondary", "error", "success"]:
        ratio = vg.calculate_contrast_ratio(color, theme["background"])
        meets_aa = vg.meets_wcag(color, theme["background"], "AA")
        meets_aaa = vg.meets_wcag(color, theme["background"], "AAA")
        
        status = "AAA ✓" if meets_aaa else ("AA ✓" if meets_aa else "✗")
        print(f"{name:12s} {color}  Ratio: {ratio:.2f}  {status}")
```

**Output:**
```text
Theme Accessibility Report

primary      #2a7cb4  Ratio: 4.53  AA ✓
secondary    #a75a27  Ratio: 5.08  AA ✓
success      #277f26  Ratio: 5.06  AA ✓
error        #d82b2b  Ratio: 4.88  AA ✓
```

##

### Example 4: Data Table with Styling

```python
import vargula

vg = vargula.Vargula()

# Create styled table
table = vg.Table(
    title="Q4 2024 Sales Report",
    caption="All figures in USD",
    title_style="bold cyan",
    border_style="blue",
    box="double",
    show_lines=True
)

table.add_column("Region", style="bold", justify="left", width=15)
table.add_column("Revenue", style="green", justify="right", width=12)
table.add_column("Growth", style="cyan", justify="center", width=10)
table.add_column("Status", justify="center", width=10)

# Add data with conditional styling
table.add_row("North America", "$1,250,000", "+15.3%", "🟢")
table.add_row("Europe", "$890,000", "+8.7%", "🟢")
table.add_row("Asia Pacific", "$1,500,000", "+22.1%", "🟢")
table.add_row("Latin America", "$450,000", "-2.4%", "🔴", style="dim")

print(table)
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-14-56.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-14-56.png?raw=true)

##

### Example 5: Multi-Progress Task Manager

```python
import vargula
import time
import random

vg = vargula.Vargula()

tasks = [
    ("Downloading files", 150),
    ("Processing data", 100),
    ("Uploading results", 80),
    ("Cleaning up", 50)
]

with vg.MultiProgress() as mp:
    # Create all tasks
    task_ids = [
        mp.add_task(desc, total=total, complete_style="green")
        for desc, total in tasks
    ]
    
    # Simulate concurrent progress
    while any(mp.tasks[tid]["progress"].current < mp.tasks[tid]["progress"].total 
              for tid in task_ids):
        for tid in task_ids:
            if mp.tasks[tid]["progress"].current < mp.tasks[tid]["progress"].total:
                mp.update(tid, random.randint(1, 5))
        time.sleep(0.05)
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-16-06.gif?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-16-06.gif?raw=true)

##

### Example 6: Color Manipulation

```python
import vargula

vg = vargula.Vargula()

base = "#3498db"

print(vg.format(f"<bold>Base Color:</bold> {base}"))
print(vg.style("█" * 40, color=base))

# Lightness variations
print(vg.format("\n<bold>Lightness:</bold>"))
for i in range(5):
    amount = (i - 2) * 0.2
    color = vg.lighten(base, amount) if amount > 0 else vg.darken(base, -amount)
    print(f"{amount:+.1f}  {color}  " + vg.style("█" * 30, color=color))

# Saturation variations
print(vg.format("\n<bold>Saturation:</bold>"))
for i in range(5):
    amount = i * 0.2
    color = vg.desaturate(base, amount)
    print(f"-{amount:.1f}  {color}  " + vg.style("█" * 30, color=color))

# Hue rotation
print(vg.format("\n<bold>Hue Rotation:</bold>"))
for degrees in [0, 60, 120, 180, 240, 300]:
    color = vg.shift_hue(base, degrees)
    print(f"{degrees:3d}°  {color}  " + vg.style("█" * 30, color=color))

# Color mixing
print(vg.format("\n<bold>Mixing with Red:</bold>"))
for weight in [0, 0.25, 0.5, 0.75, 1.0]:
    color = vg.mix("#FF0000", base, weight)
    print(f"{weight:.2f}  {color}  " + vg.style("█" * 30, color=color))
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-18-34.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-18-34.png?raw=true)
##

### Example 7: Colorblind Simulation

```python
import vargula

vg = vargula.Vargula()

colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF"]
cb_types = ["protanopia", "deuteranopia", "tritanopia"]

print(vg.format("<bold>Original Palette:</bold>"))
print(vg.preview_palette(colors, width=20, show_info=False))

for cb_type in cb_types:
    print(vg.format(f"\n<bold>{cb_type.title()} Simulation:</bold>"))
    simulated = [vg.simulate_colorblindness(c, cb_type) for c in colors]
    print(vg.preview_palette(simulated, width=20, show_info=False))
    
    is_safe, problems = vg.validate_colorblind_safety(colors, cb_type)
    if not is_safe:
        print(vg.format(f"<yellow>⚠ {len(problems)} problematic pairs</yellow>"))
```

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-18-59.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-18-59.png?raw=true)
##

##  Color Scheme Reference

### Monochromatic
Single hue with varying lightness/saturation. Creates harmonious, subtle palettes.

```python
vg.generate_palette("#3498db", "monochromatic", 5)
```

### Analogous
Adjacent colors on color wheel (±30°). Natural, comfortable combinations.

```python
vg.generate_palette("#3498db", "analogous", 5)
```

### Complementary
Opposite colors on wheel (180°). High contrast, vibrant.

```python
vg.generate_palette("#3498db", "complementary", 5)
```

### Split Complementary
Base + two colors adjacent to complement. Softer than complementary.

```python
vg.generate_palette("#3498db", "split_complementary", 5)
```

### Triadic
Three evenly spaced colors (120°). Balanced, vibrant.

```python
vg.generate_palette("#3498db", "triadic", 5)
```

### Tetradic
Four colors in two complementary pairs (60°, 180°, 240°). Rich, varied.

```python
vg.generate_palette("#3498db", "tetradic", 5)
```

### Square
Four evenly spaced colors (90°). Balanced like triadic, more colors.

```python
vg.generate_palette("#3498db", "square", 5)
```

##

##  WCAG Contrast Guidelines

| Level | Normal Text | Large Text* |
|-------|-------------|-------------|
| **AA** | 4.5:1 | 3:1 |
| **AAA** | 7:1 | 4.5:1 |

*Large text* = 18pt+ or 14pt+ bold

```python
# Check if colors meet WCAG AA
if vg.meets_wcag(text_color, bg_color, "AA"):
    print("Accessible!")

# Automatically fix contrast
accessible_color = vg.ensure_contrast(text_color, bg_color, min_ratio=4.5)
```

##

## Environment Variables

- **`NO_COLOR`**: Disable all styling (respects standard)
- **`FORCE_COLOR`**: Force enable styling even when not TTY

```bash
# Disable colors
NO_COLOR=1 python app.py

# Force colors in pipes
FORCE_COLOR=1 python app.py | less -R
```

##

##  Tips & Best Practices

### 1. **Use Themes for Consistency**
```python
vg.set_theme("dark")  # or generate custom theme
vg.write("<error>Error</error> vs <success>Success</success>")
```

### 2. **Test Accessibility Early**
```python
theme = vg.generate_accessible_theme("#3498db", wcag_level="AA")
```

### 3. **Validate for Colorblindness**
```python
is_safe, _ = vg.validate_colorblind_safety(my_colors)
```

### 4. **Save and Reuse Palettes**
```python
vg.save_palette(colors, "brand_colors.json")
# Later...
colors, _ = vg.load_palette("brand_colors.json")
```

### 5. **Nest Styles for Complex Formatting**
```python
vg.write("<bold>Bold with <red>red</red> and <blue>blue</blue></bold>")
```

##

##  Related Projects

- **[Rich](https://github.com/Textualize/rich)** - Feature-rich terminal formatting
- **[Colorama](https://github.com/tartley/colorama)** - Cross-platform ANSI colors
- **[Termcolor](https://github.com/termcolor/termcolor)** - Simple color formatting
- **[Pastel](https://github.com/sdispater/pastel)** - Color manipulation utilities

##

##  License

MIT License - see LICENSE file for details

##

##  Contributing

Contributions welcome! Please feel free to submit a Pull Request.

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/CrystallineCore/Vargula)


##

##  Acknowledgments

- Color theory based on standard color wheel harmonies
- Colorblind simulation uses Brettel, Viénot & Mollon (1997) algorithm
- WCAG contrast calculations follow WCAG 2.1 guidelines

##

**Made with 🎨 by Sivaprasad Murali**

## 
