# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = u'依瞳人工智能平台'
copyright = u'2021, thomas, Apulis AI Inc. & contributors'
author = u'Thomas, Apulis AI Inc.'
version = 'Latest'

# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#     'sphinxarg.ext',
#     'sphinxcontrib.httpdomain',
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx_markdown_tables',
    'recommonmark',
    'sphinx_rtd_theme',
]

napoleon_google_docstring = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects htmlstatic_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'Release_v1.0.md', '**.ipynb_checkpoints']

# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']
master_doc = "index"
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# html_additional_pages = {
#     'index': 'index.html',
# }

intersphinx_mapping = {
    'rtd': ('https://docs.readthedocs.io/en/stable/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
}
html_show_sourcelink = True

# html_sidebars = {
#    '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
#    'using/windows': ['windowssidebar.html', 'searchbox.html'],
# }

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True
# html_style='../static/css/custom.css'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
htmlstatic_path = ['static']
html_logo = 'static/apulis_ico.png'
html_title = '欢迎使用 (%s %s)' % (project, release)
htmlhelp_basename = "ApulisDocs"
# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# -- Options for PDF output -------------------------------------------------
latex_engine = 'xelatex'
latex_use_xindy = False
latex_show_urls = True

latex_elements = {
    'papersize':'a4',
    'pointsize':'10pt','classoptions':',oneside','babel':'',
    'inputenc':'',
    'utf8extra':'',
    'preamble': r'''
    \usepackage[UTF8, scheme = plain]{ctex}
    \addto\captionsenglish{\renewcommand{\chaptername}{}}
    \XeTeXlinebreaklocale "zh"
    \setlength{\parindent}{2em}
    \XeTeXlinebreakskip = 0pt plus 1pt
    ''',
}

latex_logo = html_logo
# Grouping the document tree into LaTeX files. List of tuples
latex_documents = [
(master_doc, 'Apulis-QIP.tex', '使用指导', 'Thomas, Apulis AI Inc.', "manual")
]