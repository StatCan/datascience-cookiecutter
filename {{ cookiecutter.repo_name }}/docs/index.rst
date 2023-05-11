.. Template created from cookiecutter.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


{{ cookiecutter.project_name_en }} documentation
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage/index
   methodology/index
   decisions/index
   reference/index
   wiki/Home

   {%- if cookiecutter.using_R == "No" %}
   .. API documentation will be generated automatically.
   
   autoapi/index
   {%- endif %}


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
