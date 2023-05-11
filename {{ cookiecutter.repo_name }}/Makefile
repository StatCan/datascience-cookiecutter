.PHONY:
	{%- if cookiecutter.using_R == "No" -%} coverage {%- endif %}
	docs
	help
	messages
	prepare_docs_folder
	requirements
	{%- if cookiecutter.using_R == "No" -%} test {%- endif %}
	wiki

# Supported CLI arguments
DOCS_SOURCEDIR	   = ./docs
DOCS_BUILDDIR      = ./docs/_build
DOCS_BUILDDIR_EN   = "$(DOCS_BUILDDIR)/en"
DOCS_BUILDDIR_FR   = "$(DOCS_BUILDDIR)/fr"
DOCS_VERSION       = -D version=`cat version;` -D release=`cat version;`

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
	find "$(DOCS_BUILDDIR)" -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} \;

# Extract translatable messages for translation
messages:
	sphinx-build -M gettext "$(DOCS_SOURCEDIR)"
	cd "$(DOCS_SOURCEDIR)"; sphinx-intl update -p _build/gettext -l fr

# Clones project's WIKI and replaces absolutes URLs for relatives
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
	sphinx-build ${DOCS_VERSION} -b html ./docs "$(DOCS_BUILDDIR_EN)"
	sphinx-build ${DOCS_VERSION} -b html ./docs "$(DOCS_BUILDDIR_FR)" -D language=fr

{%- if cookiecutter.using_R == "No" %}
# Run code coverage
coverage: requirements
	coverage run -m pytest
{%- endif %}

{%- if cookiecutter.using_R == "No" %}
# Run all the tests
test: requirements
	pytest tests/ -v -s
{%- endif %}

## Get help on all make commands; referenced from https://github.com/best-practice-and-impact/govcookiecutter
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=25 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
