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

``README.md``
^^^^^^^^^^^^^

An overview of the repository with a brief description of its purpose to inform
people what the project.


.. _detect-secrets: https://github.com/Yelp/detect-secrets
.. _cookiecutter: https://cookiecutter.readthedocs.io/
