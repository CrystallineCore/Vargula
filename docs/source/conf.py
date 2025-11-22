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
release = '1.0.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx_sitemap",
]

templates_path = ['_templates']
exclude_patterns = []

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
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# SEO-friendly meta tags
html_meta = {
    # SEO meta tags
    "description": "Vargula is a lightweight, modern Python library for beautiful terminal text styling, coloring, formatting, and UI elements.",
    "keywords": "vargula, python terminal styling, terminal colors, text formatting, ansi colors, cli ui, python color library, colorama alternative, rich alternative",
    "author": "Sivaprasad Murali",
    "robots": "index, follow",

    # Google Search Console verification
    "google-site-verification": "RA1p_5zP4s9LacW9qE1QYQ6WYLiUcYgPb1DoO91Vl4Q",

    # OpenGraph (social preview)
    "og:title": "Vargula – Terminal Text Styling for Python",
    "og:description": "Documentation, tutorials, and API reference for Vargula — a fast and intuitive Python library for terminal text styling and colored outputs.",
    "og:type": "website",
    "og:url": "https://vargula.readthedocs.io/",
    "og:image": "https://vargula.readthedocs.io/en/latest/_static/logo.png",
}

# Page title format - appears in browser tabs and search results
html_title = f"{project} {release} Documentation"

# Short title for navigation
html_short_title = "Vargula Docs"

# Favicon for brand recognition (add favicon.ico to _static folder)
# html_favicon = '_static/favicon.ico'

# Logo (add logo.png to _static folder)
html_logo = '_static/logo.png'

# Show "Created using Sphinx" in footer (optional, can help with backlinks)
html_show_sphinx = True

# Show copyright in footer
html_show_copyright = True

# Add custom CSS for additional SEO tweaks (optional)
# html_css_files = [
#     'custom.css',
# ]