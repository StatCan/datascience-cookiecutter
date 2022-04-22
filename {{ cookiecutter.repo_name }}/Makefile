.PHONY:
	coverage
	docs
	messages
	prepare_docs_folder
	requirements
	test

# Supported CLI arguments
DOCS_SOURCEDIR	   = ./docs
DOCS_BUILDDIR      = ./docs/_build
DOCS_BUILDDIR_EN   = "$(DOCS_BUILDDIR)/en"
DOCS_BUILDDIR_FR   = "$(DOCS_BUILDDIR)/fr"

# Install the Python requirements, and install pre-commit hooks
requirements:
	conda env update --file environment.yml
	pre-commit install

# Create the `docs/_build` folder or delete its contents
prepare_docs_folder:
	if [ ! -d "$(DOCS_BUILDDIR)" ]; then mkdir "$(DOCS_BUILDDIR)"; fi
	find "$(DOCS_BUILDDIR)" -mindepth 1 -maxdepth 1 -type d -exec rm -rf () \;

# Extract translatable messages for translation
messages:
	sphinx-build -M gettext "$(DOCS_SOURCEDIR)"
	sphinx-intl update -p _build/gettext -l fr

# Compile the Sphinx documentation in HTML format from a clean build
docs: prepare_docs_folder requirements
	sphinx-build -b html ./docs "$(DOCS_BUILDDIR_EN)"
	sphinx-build -b html ./docs "$(DOCS_BUILDDIR_FR)" -D language=fr

# Run code coverage
coverage: requirements
	coverage run -m pytest

# Run all the tests
test: requirements
	pytest tests/
