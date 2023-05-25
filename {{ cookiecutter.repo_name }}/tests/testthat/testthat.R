library(testthat)
library({{ cookiecutter.__pypkg }})

test_check("{{ cookiecutter.__pypkg }}", reporter = "junit")