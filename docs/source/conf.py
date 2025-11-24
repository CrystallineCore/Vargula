import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Vargula'
copyright = '2025, Sivaprasad Murali'
author = 'Sivaprasad Murali'
release = '1.1.0'
version = '1.1.0'  # Add version for better tracking

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",  # Link to other project docs
    "sphinx.ext.viewcode",     # Add links to source code
    "sphinx_sitemap",
    "sphinx.ext.napoleon",     # Support for Google/NumPy style docstrings
]

templates_path = ['_templates']
exclude_patterns = []

# Source file suffix
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document
master_doc = 'index'

# Intersphinx mapping (link to other docs)
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'rich': ('https://rich.readthedocs.io/en/stable/', None),
}

# -- SEO Configuration -------------------------------------------------------

# Base URL for sitemap generation
html_baseurl = "https://vargula.readthedocs.io/"

# Language setting for SEO
language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# Theme options for better SEO
html_theme_options = {
    'canonical_url': 'https://vargula.readthedocs.io/',
    'analytics_id': '',  # Add Google Analytics ID if you have one (e.g., 'G-XXXXXXXXXX')
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,  # Changed to True - helps users identify external links
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Navigation
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# IMPROVED: More comprehensive and keyword-rich meta tags
html_meta = {
    # Primary SEO meta tags
    "description": "Vargula - Python library for terminal text styling with color palette generation, WCAG accessibility, colorblind simulation, tables, progress bars, and intuitive markup syntax. The best alternative to Rich and Colorama for color-focused CLI applications.",
    "keywords": "vargula, python terminal styling, terminal colors, text formatting, ansi colors, cli ui, python color library, colorama alternative, rich alternative, color palette generator, wcag accessibility, colorblind simulation, terminal themes, cli styling, python cli, command line interface, terminal ui, color theory, color harmonies, ansi escape codes, cross-platform terminal, python text styling, terminal markup, progress bars, terminal tables",
    "author": "Sivaprasad Murali",
    "robots": "index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1",
    
    # Google Search Console verification
    "google-site-verification": "22G4D8fVRIvJJg67tK5fHXdhOjKv4yjXBF_E2jeATGk",
    # Viewport for mobile optimization
    "viewport": "width=device-width, initial-scale=1.0",
    
    # Language and content type
    "language": "English",
    "content-language": "en",
    
    # OpenGraph (Facebook, LinkedIn, Discord)
    "og:title": "Vargula – Python Terminal Text Styling with Color Theory",
    "og:description": "Beautiful terminal styling with color palette generation, WCAG accessibility, colorblind simulation, and intuitive markup syntax. The complete color-focused alternative to Rich and Colorama.",
    "og:type": "website",
    "og:url": "https://vargula.readthedocs.io/",
    "og:image": "https://vargula.readthedocs.io/en/latest/_static/logo.png",
    "og:image:alt": "Vargula - Python Terminal Styling Library",
    "og:site_name": "Vargula Documentation",
    "og:locale": "en_US",
    
    # Twitter Card (X)
    "twitter:card": "summary_large_image",
    "twitter:title": "Vargula – Python Terminal Text Styling Library",
    "twitter:description": "Color palette generation, WCAG accessibility, colorblind simulation, tables, progress bars. The best Python library for accessible terminal styling.",
    "twitter:image": "https://vargula.readthedocs.io/en/latest/_static/logo.png",
    
    # Additional helpful meta tags
    "theme-color": "#2980B9",
    "apple-mobile-web-app-capable": "yes",
    "apple-mobile-web-app-status-bar-style": "black",
}

# Page title format - appears in browser tabs and search results
html_title = f"{project} {release} Documentation"

# Short title for navigation
html_short_title = "Vargula Docs"

# Favicon for brand recognition (add favicon.ico to _static folder)
html_favicon = '_static/favicon.ico'

# Logo (add logo.png to _static folder)
html_logo = '_static/logo.png'

# Show "Created using Sphinx" in footer
html_show_sphinx = True

# Show copyright in footer
html_show_copyright = True

# Last updated timestamp
html_last_updated_fmt = '%b %d, %Y'

# Add custom CSS/JS for additional features
html_css_files = [
    'custom.css',  # Add custom styles if needed
]

html_js_files = [
    # Add custom JavaScript if needed (e.g., for analytics)
]

# -- Sitemap Configuration ---------------------------------------------------

# Sitemap settings for better crawling
sitemap_url_scheme = "{link}"  # Use clean URLs without .html extension in sitemap

# Additional locales for sitemap (if you plan multilingual docs)
# sitemap_locales = [None, 'en']

# -- Additional SEO Best Practices -------------------------------------------

# 1. Ensure all pages are linked (no orphan pages)
# Sphinx will warn about orphan pages - fix these warnings

# 2. Use descriptive filenames for .rst/.md files
# Example: 'color-palette-generation.rst' instead of 'cpg.rst'

# 3. Add structured data (JSON-LD) in _templates/layout.html
# This helps search engines understand your content better

# 4. Create robots.txt in your source folder with:
# User-agent: *
# Allow: /
# Sitemap: https://vargula.readthedocs.io/sitemap.xml

# 5. Use descriptive section headers (H1, H2, H3) in your docs
# Search engines use these to understand content structure

# -- MyST Parser Configuration (for Markdown) --------------------------------

myst_enable_extensions = [
    "colon_fence",      # ::: for fenced blocks
    "deflist",          # Definition lists
    "html_image",       # HTML image tags
    "linkify",          # Auto-detect URLs
    "replacements",     # Text replacements
    "smartquotes",      # Smart quotes
    "substitution",     # Variable substitutions
    "tasklist",         # Task lists [ ] [x]
]

# -- Code Documentation Configuration ----------------------------------------

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Napoleon settings for docstring parsing
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- Performance Optimizations -----------------------------------------------

# Generate source links to GitHub (helps with credibility)
html_context = {
    "display_github": True,
    "github_user": "crystallinecore",  # Your GitHub username
    "github_repo": "vargula",          # Your repo name
    "github_version": "main",          # Branch name
    "conf_py_path": "/docs/source/",   # Path to docs source
}

# Show source link
html_show_sourcelink = True

# Copy button for code blocks (requires sphinx-copybutton extension if you want this)
# Add to extensions: "sphinx_copybutton"

# -- External Links Configuration --------------------------------------------

# Mark external links with icon (helps users and search engines)
# html_use_opensearch = 'https://vargula.readthedocs.io'  # Add OpenSearch

# -- Additional Recommendations ----------------------------------------------

# TODO: After implementing these configs, also:
# 1. Submit sitemap to Google Search Console: https://search.google.com/search-console
# 2. Submit sitemap to Bing Webmaster Tools: https://www.bing.com/webmasters
# 3. Add structured data (JSON-LD) for SoftwareApplication
# 4. Create a _templates/layout.html to add JSON-LD structured data
# 5. Monitor with Google Analytics
# 6. Use descriptive file names for all .rst files
# 7. Ensure all pages have proper H1 headers
# 8. Add alt text to all images
# 9. Use internal linking between related pages
# 10. Keep URLs clean and descriptive (Sphinx handles this automatically)