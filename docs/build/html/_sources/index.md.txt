# Vargula Documentation

Welcome to the official documentation for Vargula.


```{toctree}
:maxdepth: 2
:caption: Contents:

comparison
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
faq
```


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
