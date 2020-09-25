import pathlib
import sys
from datetime import datetime

import caproto
import caproto.docs
import sphinx_rtd_theme  # noqa: F401

module_path = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(module_path))


# -- Project information -----------------------------------------------------
project = '{{ cookiecutter.project_name }}'
author = '{{ cookiecutter.author_name }}'
copyright = f'{datetime.now().year}, {author}'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''

# -- General configuration ---------------------------------------------------

needs_sphinx = '3.2.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'numpydoc',
    'doctr_versions_menu',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = [caproto.docs.templates.PATH]

# The suffix(es) of source filenames.
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Extension configuration -------------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Extension configuration -------------------------------------------------

autodoc_default_options = {
    **caproto.docs.autodoc_default_options,
}

intersphinx_mapping = {
    # 'ophyd': ('https://blueskyproject.io/ophyd', None),
    'python': ('https://docs.python.org/3', None),
    # 'numpy': ('https://docs.scipy.org/doc/numpy', None),
    'caproto': ('https://caproto.github.io/caproto/master', None),
}

# Generate summaries:
autosummary_generate = True

# Duplicate attributes will be generated without this:
autoclass_content = 'init'

# Tons of warnings will be emitted without this:
numpydoc_show_class_members = False

autosummary_context = {
    **caproto.docs.autosummary_context,
    # The default assumes your repository root is one level up from conf.py.
    # If that is not accurate, uncomment and modify the following line:
    # 'project_root': '..',
}

html_context = {
    **autosummary_context,
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
    ],
}


def setup(app):
    caproto.docs.setup(app)
