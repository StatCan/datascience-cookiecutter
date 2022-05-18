# `docs` folder overview

All documentation for the project should be included in this folder with
acceptable formatting for Sphinx. Support for both reStructuredText and Markdown
is available.

If you want any documentation written in the {{ cookiecutter.repo_name }} folder
without duplicating it, include it in the docs/{{ cookiecutter.repo_name }} folder.

To build the documentation locally run

```sh
sphinx-build -b html ./docs ./docs/_build
```

The HTML outputs will be available at `docs/_build/index.html`.
