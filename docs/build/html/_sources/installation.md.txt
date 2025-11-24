# Installation

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Install from PyPI

The easiest way to install Vargula is using pip:

```bash
pip install vargula
```

### Upgrade to Latest Version

To upgrade to the latest version:

```bash
pip install --upgrade vargula
```

### Install Specific Version

To install a specific version:

```bash
pip install vargula==1.1.0
```

## Install from Source

Clone the repository and install in development mode:

```bash
git clone https://github.com/crystallinecore/vargula.git
cd vargula
pip install -e .
```

This allows you to modify the source code and see changes immediately.

## Verify Installation

Check that Vargula is installed correctly:

```python
import vargula as vg
print(vg.__version__)
# Output: 1.1.0
```

Test basic functionality:

```python
import vargula as vg

# Test color output
print(vg.style("Hello, Vargula!", color="cyan", look="bold"))

# Test markup
vg.write("<red>Red text</red> and <blue>blue text</blue>")

# Test palette generation
palette = vg.generate_palette("#3498db", "complementary", 3)
print(palette)
```

If you see colored output, everything is working correctly!

## Platform-Specific Notes

### Windows

Vargula automatically enables ANSI color support on Windows 10 and later. For older versions of Windows:

- Use **Windows Terminal** (recommended)
- Or enable ANSI support in Command Prompt manually
- Or use **ConEmu** or similar terminal emulators

```python
# Vargula handles this automatically
import vargula as vg
# Colors work out of the box on Windows 10+
```

### macOS

No additional setup required. Works perfectly in:
- Terminal.app
- iTerm2
- Any other macOS terminal emulator

### Linux

No additional setup required. Works in all modern terminal emulators:
- GNOME Terminal
- Konsole
- xterm
- Alacritty
- kitty
- And many more

## Dependencies

Vargula has **zero external dependencies**. It uses only Python standard library modules:

- `sys` - System-specific parameters
- `os` - Operating system interfaces
- `re` - Regular expressions
- `colorsys` - Color system conversions
- `json` - JSON encoding/decoding
- `pathlib` - Object-oriented filesystem paths
- `contextlib` - Context manager utilities
- `typing` - Type hints support
- `random` - Random number generation

This means:
- ✓ Fast installation
- ✓ No dependency conflicts
- ✓ Minimal security surface
- ✓ Works anywhere Python works

## Virtual Environment (Recommended)

It's recommended to use a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Vargula
pip install vargula
```

## Development Installation

For contributors and developers:

```bash
# Clone repository
git clone https://github.com/crystallinecore/vargula.git
cd vargula

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Check code quality
flake8 vargula
```

## Uninstallation

To remove Vargula:

```bash
pip uninstall vargula
```

## Troubleshooting

### Colors Not Showing

If colors aren't displaying:

1. **Check if output is a TTY:**
   ```python
   import sys
   print(sys.stdout.isatty())  # Should be True
   ```

2. **Force color output:**
   ```bash
   FORCE_COLOR=1 python your_script.py
   ```

3. **Check NO_COLOR variable:**
   ```bash
   # Make sure NO_COLOR is not set
   echo $NO_COLOR
   ```

### Windows ANSI Issues

If colors don't work on Windows:

1. Update to Windows 10 or later
2. Use Windows Terminal instead of cmd.exe
3. Try forcing ANSI support:
   ```python
   import vargula as vg
   vg.enable()  # Force enable colors
   ```

### Import Errors

If you get import errors:

```bash
# Check Python version
python --version  # Should be 3.7+

# Verify installation
pip show vargula

# Reinstall
pip uninstall vargula
pip install vargula
```

## Next Steps

Now that Vargula is installed, continue with:

- [Quick Start Guide](quick-start.md) - Learn the basics in 5 minutes
- [Core Concepts](core-concepts.md) - Understand key concepts
- [API Reference](../api/index.md) - Browse all functions
- [Examples](../examples/index.md) - See real-world usage