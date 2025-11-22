# Conventions

Vargula supports inline color styling using intuitive tag syntax:

- **`<#hexcode>`** - Set foreground (text) color using hex codes
- **`<@#hexcode>`** - Set background color using hex codes
- **`<colorname>`** - Apply named foreground color (e.g., `red`, `blue`, `bright_green`)
- **`<@colorname>`** - Apply named background color (e.g., `<@red>`, `<@yellow>`)
- **`<lookname>`** - Apply text style (e.g., `bold`, `italic`, `underline`)
- **`<customname>`** - Apply custom styles created with `create()`

## Tag Format Rules

- **Hex codes** can be 3 or 6 characters: `<#F00>` or `<#FF0000>`
- **The `#` prefix** is for foreground hex colors: `<#FF5733>`
- **The `@` prefix** is required for all background colors (named or hex): `<@yellow>`, `<@FF0000>`
- **Tags are case-insensitive** for named colors: `<red>` and `<RED>` work the same
- **Closing tags** must match opening tags exactly: `<@yellow>...</@yellow>`
- **Tags can be nested** arbitrarily deep for complex styling

## Available Named Colors

**Standard colors:** `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`

**Bright variants:** `bright_black`, `bright_red`, `bright_green`, `bright_yellow`, `bright_blue`, `bright_magenta`, `bright_cyan`, `bright_white`

**Text styles:** `bold`, `dim`, `italic`, `underline`, `blink`, `reverse`, `hidden`, `strikethrough`

## Examples

```py
from vargula import write

# Named foreground colors
write("<red>Red text</red>")
write("<bright_blue>Bright blue text</bright_blue>")

# Named background colors
write("<@yellow>Yellow background</@yellow>")
write("<@red>Red background</@red>")
write("<@bright_black>Dark background</@bright_black>")

# Hex foreground color
write("<#FF5733>Orange text</#FF5733>")
write("<#3498db>Blue text</#3498db>")

# Hex background color
write("<@#FF0000>Red background</@#FF0000>")
write("<@#F00>Short hex red background</@#F00>")

# Foreground + background combination
write("<#FFFFFF><@#000000>White text on black</@#000000></#FFFFFF>")
write("<green><@black>Green on black</@black></green>")

# Mix with text styles
write("<bold><#00FF00><@#000080>Bold green on navy</@#000080></#00FF00></bold>")
write("<italic><@yellow>Italic on yellow</@yellow></italic>")

# Nested backgrounds
write("<@yellow>Yellow <@red>then red</@red> back to yellow</@yellow>")
write("<@#FF0000>Hex red <@yellow>named yellow</@yellow> back to hex</@#FF0000>")

# Complex nesting
write("<bold><red>Bold <italic>and italic</italic> red text</red></bold>")
```

**Output:**

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2022-53-32.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2022-53-32.png?raw=true)

