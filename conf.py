# -- General configuration ------------------------------------------------

extensions = [
]

locale_dirs = ['locale/']
gettext_compact = False

# The base toctree document.
master_doc = "index"

# General information about the project.
project = "Sphinx Playground"
copyright = "2021, Oriol Abril-Pla"
author = "Oriol Abril-Pla"

version = "0.1"
# The full version, including alpha/beta/rc tags.
release = version

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store", ".ipynb_checkpoints",
    "README.md", ".virtual_documents", "jupyter_execute"
]


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
html_static_path = ["_static"]
html_js_files = ["readthedocs.js"]
