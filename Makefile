.PHONY:
	coverage
	docs
	docs_messages
	help
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
