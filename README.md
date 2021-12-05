# ctsimu-scenarios
A file format to describe CT scans.


This is the source code of the file format documentation. You need the Python package [Sphinx](https://www.sphinx-doc.org) to compile it.

The [Read the Docs theme](https://sphinx-rtd-theme.readthedocs.io) is required. To install it, use:

    pip install sphinx_rtd_theme

Additionally the [sphinxcontrib-bibtex](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/quickstart.html) extension is required. To install it, use:

    pip install sphinxcontrib-bibtex
    
The references.bib file can be edited with a reference manager like [JabRef](https://www.jabref.org/).

## Compile and deploy

The source files are all located in the `source` folder. To create the HTML documentation and store it in the `build` folder, run

    make html

To create a PDF version using LaTeX, run

	make latexpdf

To build everything anew from scratch, delete the `build` folder or run

    make clean

Github Pages expects the HTML documentation in a folder called `docs`. You can run the deploy script to automatically copy the content from `build/html` to `docs` and create the necessary `.nojekyll` file.

    deploy.bat (Windows)
    ./deploy.sh (Linux)
