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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'CTSimU Scenarios'
copyright = 'WIPANO CTSimU Project'
author = 'WIPANO CTSimU Project'

# The full version, including alpha/beta/rc tags
release = '1.2'

title = "CTSimU Scenario Descriptions {version}".format(version=release)

# -- General configuration ---------------------------------------------------

# The html index document.
root_doc = 'index'

# The latex index document
latex_documents = [
	("index_latex", "ctsimu-scenarios_{version}.tex".format(version=release), title, author, "manual", False),
	]


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	"sphinx_rtd_theme",
	"sphinx.ext.autosectionlabel",
	"sphinxcontrib.bibtex",
	"sphinx.ext.imgmath"   # to render equations as PNG images and avoid externally loaded JavaScript libraries
]

# Add the path of a bibliography (.bib) file
bibtex_bibfiles = ['library.bib']

# Define bibtex enconding (default: utf-8-sig)
bibtex_encoding = 'utf-8-sig'

# Define bibtex style
bibtex_default_style = 'unsrt'

imgmath_image_format = "svg"
imgmath_font_size = 12
imgmath_latex_preamble = """\\usepackage{sansmathfonts}
\\usepackage{paratype}
\\usepackage{amsmath, amssymb}
\\usepackage{sfmath}
\\usepackage{sansmath}
"""

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Change autoconfigextension default behaviour for section labels, in order to
# avoid duplicate label summary warnings.
# Source: https://www.spinics.net/lists/linux-doc/msg77015.html
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 1

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Figures with numbers:
numfig = True
numfig_format = {
	"figure":     "Fig. %s",
	"table":      "Tab. %s",
	"code-block": "Listing %s",
	"section":    "Sec. %s"
}

# Our own global roles (commands accesible in all .rst files):
rst_prolog = """
.. |nbsp| unicode:: 0xA0
    :trim:

.. role:: json(code)
  :language: json-object
  :class: highlight

"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Copyright is handled by extra footer - _templates/footer.html
html_show_copyright = False

# -- Options for LaTeX output -------------------------------------------------
latex_engine = 'pdflatex'
latex_toplevel_sectioning = 'section'  # part, section or chapter
latex_theme = 'manual'
latex_docclass = {
   'howto': 'scrartcl',
   'manual': 'scrartcl'
}
latex_elements = {
	'papersize': 'a4paper',
	'pointsize': '11pt',
	'fontpkg': r'''
		\usepackage{paratype}
		\usepackage[scaled=0.72]{beramono}   % For Code
	''',
	'preamble': r"""
		\usepackage{graphicx}
		\usepackage{parskip}
		\usepackage{amsmath, amssymb}
		\usepackage{gensymb}	% degree symbol
		\usepackage{array}
		\usepackage{upgreek} % gerade griechische Buchstaben
		\usepackage{listings}   % code listings
		\usepackage{enumitem}	% alphabetical enumerate lists
		\usepackage{booktabs}	% for tables
		\newcommand{\SI}[2]{#1\,\text{#2}}
		\usepackage{setspace}	% line spacings
		\usepackage{wrapfig}
		\usepackage{datetime}
		\usepackage{doi}

		\usepackage{sfmath} % sans serif math
		\DeclareMathSymbol{\Delta}{\mathalpha}{SFMathGreek}{"01}
		%\SetSymbolFont{operators}{normal}{\math@encoding}{\math@sfdefault}{m}{n}
		%\SetSymbolFont{operators}{bold}{\math@encoding}{\math@sfdefault}{bx}{n}

		% % Captions and figures in sans-serif, including math:
		\usepackage[font=sf, textfont=sf, normalsize, labelfont={sf,bf}, skip=0.33\baselineskip]{caption}	% captions in sans-serif
		\usepackage{float} % to easily modify floats
		\usepackage{etoolbox} % nice command patching
		\usepackage[EULERGREEK]{sansmath} % sans serif math
		\usepackage{everyhook} % nice \every... patching
		% restyle figures to make \everymath=\sansmath (float package)
		\restylefloat{figure}
		\floatevery{figure}{\PushPreHook{math}{\sansmath}}
		% undo the change to \everymath at the end of the figure (etoolbox)
		\apptocmd{\endfigure}{\PopPreHook{math}}{}{}

		\renewcommand{\figurename}{Fig.}
		\renewcommand{\tablename}{Tab.}

		\usepackage{hyperref}
		\hypersetup{
			pdftitle    = {"""+title+r"""},
			pdfsubject  = {},
			pdfauthor   = {"""+author+r"""},
			pdfkeywords = {CT, scenario, simulation, CTSimU},
			colorlinks  = {false},
			pdfborder   = {0 0 0}  % Keine Rahmen um Links
		}

		\newdateformat{ymddate}{\THEYEAR-\twodigit{\THEMONTH}-\twodigit{\THEDAY}}

		% Header
		\usepackage{fancyhdr}
		\pagestyle{fancy}
		\fancyhf{}
		\fancyhead[CE,CO]{\leftmark}
		\fancyfoot[CE,CO]{\thepage}


		\usepackage{newunicodechar}
		\newunicodechar{≤}{\ensuremath{\leq}}
		\newunicodechar{≥}{\ensuremath{\geq}}
		\newunicodechar{⋅}{\ensuremath{\cdot}}
		\newunicodechar{≈}{\ensuremath{\approx}}
		\newunicodechar{×}{\ensuremath{\times}}
		\newunicodechar{→}{\ensuremath{\rightarrow}}
		\newunicodechar{°}{\ensuremath{^\circ}}
		\newunicodechar{²}{\textsuperscript{2}}
		\newunicodechar{³}{\textsuperscript{3}}

		\newunicodechar{α}{\ensuremath{\alpha}}
		\newunicodechar{β}{\ensuremath{\beta}}
		\newunicodechar{γ}{\ensuremath{\gamma}}
		\newunicodechar{δ}{\ensuremath{\delta}}
		\newunicodechar{ϵ}{\ensuremath{\epsilon}}
		\newunicodechar{ε}{\ensuremath{\varepsilon}}
		\newunicodechar{ζ}{\ensuremath{\zeta}}
		\newunicodechar{η}{\ensuremath{\eta}}
		\newunicodechar{θ}{\ensuremath{\theta}}
		\newunicodechar{ϑ}{\ensuremath{\vartheta}}
		\newunicodechar{ι}{\ensuremath{\iota}}
		\newunicodechar{κ}{\ensuremath{\kappa}}
		\newunicodechar{λ}{\ensuremath{\lambda}}
		\newunicodechar{μ}{\ensuremath{\mu}}
		\newunicodechar{ν}{\ensuremath{\nu}}
		\newunicodechar{ξ}{\ensuremath{\xi}}
		\newunicodechar{π}{\ensuremath{\pi}}
		\newunicodechar{ρ}{\ensuremath{\rho}}
		\newunicodechar{σ}{\ensuremath{\sigma}}
		\newunicodechar{τ}{\ensuremath{\tau}}
		\newunicodechar{υ}{\ensuremath{\upsilon}}
		\newunicodechar{φ}{\ensuremath{\phi}}
		\newunicodechar{ϕ}{\ensuremath{\varphi}}
		\newunicodechar{χ}{\ensuremath{\chi}}
		\newunicodechar{ψ}{\ensuremath{\psi}}
		\newunicodechar{ω}{\ensuremath{\omega}}

		\newunicodechar{Γ}{\ensuremath{\Gamma}}
		\newunicodechar{Δ}{\ensuremath{\Delta}}
		\newunicodechar{Θ}{\ensuremath{\Theta}}
		\newunicodechar{Λ}{\ensuremath{\Lambda}}
		\newunicodechar{Ξ}{\ensuremath{\Xi}}
		\newunicodechar{Π}{\ensuremath{\Pi}}
		\newunicodechar{Σ}{\ensuremath{\Sigma}}
		\newunicodechar{ϒ}{\ensuremath{\Upsilon}}
		\newunicodechar{Φ}{\ensuremath{\Phi}}
		\newunicodechar{Ψ}{\ensuremath{\Psi}}
		\newunicodechar{Ω}{\ensuremath{\Omega}}
	""",
	'maketitle': r"""
\begin{titlepage}
\begin{wrapfigure}[0]{r}{0.1\textwidth}
\includegraphics[scale=4.0]{fileformat_logo.pdf}
\end{wrapfigure}
{\ymddate\today}

\par ~

\par ~

\par ~

\par ~

\par ~

\begin{spacing}{2.0}
{\Huge {CTSimU Scenario Descriptions}}

{\LARGE {A data format specification in JSON}}

Version """+release+r"""
\end{spacing}

\par ~

\par ~

\par ~

{\Large {WIPANO CTSimU Project}}

\emph{Radiographic Computed Tomography Simulation for Measurement Uncertainty Evaluation}

\par ~

\par ~

\par ~

\par ~

\textbf{Summary:}
This is the specification for a JSON file format to handle the parameters of a full industrial CT scan scenario, intended for describing virtual CT scenarios for simulations, as well as for documenting real CT scan geometries and acquisition parameters and their measurement uncertainties.

\par ~

\par ~

This specification is free to use. It is released under the \textbf{Apache 2.0 license}.\\
You can find the \textbf{online version} of this document at\\
\url{https://bamresearch.github.io/ctsimu-scenarios}

\end{titlepage}
"""
}