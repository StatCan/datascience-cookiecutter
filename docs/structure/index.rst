``datascience-cookiecutter`` structure
======================================

The repository structure is made up of the following components:

.. toctree::
    :maxdepth: 2

    docs
    cookiecutter.repo_name

Top-level files
---------------

In addition to the folders idenfied above, the following files are also used.

``.secrets.baseline``
^^^^^^^^^^^^^^^^^^^^^

This provides a baseline for `detect-secrets`_. When paired with ``pre-commit``,
``detect-secrets`` helps prevent secrets from being committed to the repository.
The baseline file flags secret-like data that the user deliberatly wants to allow
to commit to the repository.

``cookiecutter.json``
^^^^^^^^^^^^^^^^^^^^^

A :abbr:`JSON (JavaScript Object Notation)` file containing the prompts and
default values during template generation. Any keys in the file that begin with
an underscore are not shown to users.

For more information, see the `cookiecutter`_ package documentation.

``pyproject.toml``
^^^^^^^^^^^^^^^^^^

A :abbr:`TOML (Tom's Obvious Minimal Language)` file for `PEP 518`_ Python project
configuration. At a minimum this file is used to specify the build system of the project,
but can also be used for configuration for additional packages.

.. note::

    This file replaces the :file:`setup.py` file original used by setuptools.

More information can be found in the `Python packaging user guide`_ and `pip specific`_
documentation.

``README.md``
^^^^^^^^^^^^^

An overview of the repository with a brief description of its purpose to inform
people what the project.

``setup.cfg``
^^^^^^^^^^^^^

A configuration file to provide static metadata used by setuptools. This provides
information such as the name and version of the package, but can also be used to provide
additional metadata necessary when publishing a package.

More information can be found in the `Python packaging user guide`_.

.. _detect-secrets: https://github.com/Yelp/detect-secrets
.. _cookiecutter: https://cookiecutter.readthedocs.io/
.. _PEP 518: https://peps.python.org/pep-0518/
.. _Python packaging user guide: https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata
.. _pip specific: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
