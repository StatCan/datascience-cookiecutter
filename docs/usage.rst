Using the template
==================

You can quickly initialize a new data science project using the steps outlined below.
Before you get started, there are a couple base requirements to make sure you'll be
successful.

Initial setup
-------------

To set yourself up for success, ensure your system is ready to use the template.

Required software
^^^^^^^^^^^^^^^^^

This project is based on `cookiecutter`_, but we recommend `cruft`_ to help keep your
project in sync as the templates evolve to provide additional usaful features.

``cruft`` can be installed through ``pip``::

    pip install cruft
    or
    conda install cruft

Git configuration
^^^^^^^^^^^^^^^^^

While not strictly required for the template, it is *strongly* recommended that you
manage your projects through ``git``. This is a requirement for all Data Science
Division projects.

Make sure your git client is configured appropriately::

    git config --global user.name "FIRST_NAME LAST_NAME"
    git config --global user.email "MY_NAME@statcan.gc.ca"

Start a new project
-------------------

In a terminal, navigate to your desired working directory. The template will create a
project directory for you, so no need to do that manually.

Initialize a new project:

.. code-block:: sh

    $ cruft create https://github.com/StatCan/datascience-cookiecutter

You'll be asked some questions, like the project name, organization name, repository name,
etc. To accept any of the default responses just hit enter, otherwise provide the
information as appropriate.

After you answer all the questions it will create an initial project structure for you.
Navigate into the top level folder::

.. code-block:: sh

    $ cd <repository name>

Git project initialization
^^^^^^^^^^^^^^^^^^^^^^^^^^

At this point you can finalize the ``git`` configuration for the project and commit your
initial set of files:

.. code-block:: sh

    $ git init .
    $ git add -A
    $ git commit -m "Initialize project"
    $ git remote add origin <gitlab project url> # https://gitlab.k8s.cloud.statcan.ca/datascience-division/[subgroup]/[project_repo].git
    $ git push --set-upstream origin main

Conda environment creation
^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that ``git`` is ready you can configure your development environment for the project:

.. code-block:: sh

    $ conda env create -f conda-envs/environment.<repo name>-docs.yml
    $ conda activate <repo name>

The templates assume you're creating a package. The easiest way to work on your project
is to install it into your environment as an editable install:

.. code-block:: sh

    $ pip install -e .

Now as you write code or move between branches your environment will always reflect the
latest source code.

Keep up to date with the templates
----------------------------------

The templates are constantly evolving to reflect the best practices of data science at
Statistics Canada. You can use ``cruft`` to keep up to date and synchronize the changes
without breaking your current project.

Check if there are changes to the templates that you don't have::

    $ cruft check

If ``cruft`` tells you that there are changes you can inspect them to see what has changed::

    $ cruft diff

To update your project with the latest template files::

    $ cruft update

To see all that ``cruft`` has to offer you should refer to the `cruft`_ documentation.

.. cookiecutter: https://cookiecutter.readthedocs.io/en/stable/
.. cruft: https://cruft.github.io/cruft/