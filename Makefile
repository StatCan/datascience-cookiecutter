.PHONY:
	coverage
	docs
	docs_messages
	prepare_docs_folder
	requirements

# Supported CLI arguments
DOCS_SOURCEDIR	   = ./docs
DOCS_BUILDDIR      = ./docs/_build

# Install the Python requirements, and install pre-commit hooks
requirements:
	conda env update --file environment.yml
	pre-commit install

# Create the `docs/_build` folder or delete its contents
prepare_docs_folder:
	if [ ! -d ""$(DOCS_BUILDDIR)"" ]; then mkdir "$(DOCS_BUILDDIR)"; fi
	find "$(DOCS_BUILDDIR)" -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} \;

# Compile the Sphinx documentation in HTML format from a clean build
docs: prepare_docs_folder requirements
	sphinx-build -b html "${DOCS_SOURCEDIR}" "${DOCS_BUILDDIR}"

# Extract translatable messages in docs
docs_messages: prepare_docs_folder
	sphinx-build -M gettext "${DOCS_SOURCEDIR}" "$(DOCS_BUILDDIR)"
	cd "${DOCS_SOURCEDIR}"; sphinx-intl update -p _build/gettext -l fr

# Run code coverage
coverage: requirements
	coverage run -m pytest
