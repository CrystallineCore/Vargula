# ============================================
# File: vargula/__init__.py
# ============================================
"""
vargula - Simple cross-platform terminal text styling library with advanced color palette generation
"""

# Import main class and types
from .vargula import (
    # Main class
    Vargula,
    
    # Type definitions
    PaletteScheme,
    ColorBlindType,
    
    # Constants
    COLORS,
    BG_COLORS,
    LOOKS,
    
    # Metadata
    __version__,
)

# Package metadata
__author__ = "Sivaprasad Murali"
__email__ = "sivaprasad.off@example.com"
__license__ = "MIT"
__description__ = "Simple cross-platform terminal text styling library with advanced color palette generation"
__url__ = "https://github.com/crystallinecore/vargula"

__all__ = [
    # Main class
    "Vargula",
    
    # Type definitions
    "PaletteScheme",
    "ColorBlindType",
    
    # Constants
    "COLORS",
    "BG_COLORS",
    "LOOKS",
    
    # Helper function
    "progress_bar",
    
    # Metadata
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__description__",
    "__url__",
]