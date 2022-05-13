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

# Variables for automatically include projects wiki into doc
WIKIDIR       = ./docs/wiki
REPO          = $(basename $(shell git config --get remote.origin.url))
PROJECT       = $(lastword $(subst /, ,$(REPO)))
WIKI          = $(REPO).wiki.git
GITLAB_URL    = $(subst /,\/,$(REPO)/-/wikis/)
GITHUB_URL    = $(subst /,\/,$(REPO)/wiki/)


# Install the Python requirements
requirements: .git/hooks/pre-commit
	conda env update --prune --file environment.yml

# Install pre-commit hooks
.git/hooks/pre-commit:
	pre-commit install

# Create the `docs/_build` folder or delete its contents
prepare_docs_folder:
	if [ ! -d "$(DOCS_BUILDDIR)" ]; then mkdir "$(DOCS_BUILDDIR)"; fi
	find "$(DOCS_BUILDDIR)" -mindepth 1 -maxdepth 1 -type d -exec rm -rf () \;

# Extract translatable messages for translation
messages:
	sphinx-build -M gettext "$(DOCS_SOURCEDIR)"
	sphinx-intl update -p _build/gettext -l fr

# Clones project's WIKI and replaces absolutes URLs for relatives
# NOTE: I will also mv README.md ./docs/usage/index.md
wiki:
	git clone $(WIKI) 
	rm -rf $(WIKIDIR); mv $(PROJECT).wiki $(WIKIDIR)
	if [[ "$(WIKI)" == *"https://gitlab.com"* ]]; then \
		find $(WIKIDIR) -type f -name "*.md" -exec sed -i -e "s/$(GITLAB_URL)//g" {} \; ; \
	fi 
	if [[ "$(WIKI)" == *"https://github.com"* ]]; then \
		find $(WIKIDIR) -type f -name "*.md" -exec sed -i -e "s/$(GITHUB_URL)//g" {} \; ; \
	fi

# Compile the Sphinx documentation in HTML format from a clean build
docs: prepare_docs_folder requirements
	cp ./docs/_splashpage/index.html "${DOCS_BUILDDIR}/index.html"
	sphinx-build -b html ./docs "$(DOCS_BUILDDIR_EN)"
	sphinx-build -b html ./docs "$(DOCS_BUILDDIR_FR)" -D language=fr

# Run code coverage
coverage: requirements
	coverage run -m pytest

# Run all the tests
test: requirements
	pytest tests/
