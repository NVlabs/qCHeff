# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "qCHeff"
copyright = "2024, Abhishek Chakraborty"
author = "Abhishek Chakraborty"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autodoc2",
    "sphinx.ext.napoleon",
    "myst_parser",
]

autodoc2_packages = ["../src/qcheff"]
autodoc2_render_plugin = "myst"

myst_enable_extensions = [
  "colon_fence",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]


add_module_names = False
modindex_common_prefix = ["qcheff."]