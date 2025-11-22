# Vargula Documentation

Welcome to the official documentation for Vargula.


```{toctree}
:maxdepth: 2
:caption: Contents:

installation
conventions
api
inbuilt
color_scheme
wcag
env_var
examples
tips
appendix
reference
```

## What is Vargula?

Vargula is a powerful Python library for terminal styling that combines better functionality with comprehensive color theory tools. Style your terminal output with colors, create beautiful tables, show progress bars, and generate harmonious color palettes - all with a simple, intuitive API.

Try [this](https://pastebin.com/BpGDZkfu) Vargula's code snippet to run this:

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-46-17.gif?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-46-17.gif?raw=true)


## What's new?

### Added
- **Background color tag syntax**: New `<@color>` tag convention for inline background styling
  - Hex background colors: `<@#FF0000>text</@#FF0000>`, `<@#F00>text</@#F00>`
  - Named background colors: `<@red>text</@red>`, `<@yellow>text</@yellow>`
  - Full symmetry with foreground color tags

### Enhanced
- **`format()` function**: Enhanced tag parsing to support background color syntax
  - Proper validation of hex color codes (3 or 6 characters)
  - Maintains full backward compatibility with existing tags

Refer the *Tag Syntax Conventions* section to know more.

##  Features

-  **Text Styling**: Colors, backgrounds, and text decorations (bold, italic, underline, etc.)
-  **Markup Syntax**: HTML-like tags for inline styling (`<red>error</red>`)
-  **Tables**: Rich-style tables with customizable borders and styling
-  **Progress Bars**: Customizable progress indicators with ETA and rate display
-  **Color Palettes**: Generate harmonious color schemes based on color theory
-  **Accessibility**: WCAG contrast checking and colorblind simulation
-  **Themes**: Built-in themes and custom theme support
-  **Cross-platform**: Works on Windows, macOS, and Linux


