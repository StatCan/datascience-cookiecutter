.PHONY:
	coverage
	docs
	prepare_docs_folder

# Supported CLI arguments
DOCS_BUILDDIR      = ./docs/_build

# Install the Python requirements, and install pre-commit hooks
requirements:
	python -m pip install -U pip setuptools
	python -m pip install -r requirements.txt
	pre-commit install

# Create the `docs/_build` folder or delete its contents
prepare_docs_folder:
	if [ ! -d "${DOCS_BUILDDIR}" ]; then mkdir "${DOCS_BUILDDIR}"; fi
	find "${DOCS_BUILDDIR}" -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} \;

# Compile the Sphinx documentation in HTML format from a clean build
docs: prepare_docs_folder requirements
	sphinx-build -b html ./docs "${DOCS_BUILDDIR}"

# Run code coverage
coverage: requirements
	coverage run -m pytest
