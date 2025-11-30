# Conventions

Vargula supports inline color styling using intuitive tag syntax:

- **`<#hexcode>`** - Set foreground (text) color using hex codes
- **`<@#hexcode>`** - Set background color using hex codes
- **`<colorname>`** - Apply named foreground color (e.g., `red`, `blue`, `bright_green`)
- **`<@colorname>`** - Apply named background color (e.g., `<@red>`, `<@yellow>`)
- **`<lookname>`** - Apply text style (e.g., `bold`, `italic`, `underline`)
- **`<customname>`** - Apply custom styles created with `create()`
- **`\\<tag>`** - Ignores the tag and prints as is. 
- **`\<tag>`** - Ignores the tag and prints as is, if used as a raw string. (i.e. `r"\<tag>"`) 

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
