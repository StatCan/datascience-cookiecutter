# `src` package overview

All functions in this project should be stored in this folder. All tests belong in the 
`tests` folder, which is one level above, in the main project directory.

It is strongly recommended that you import functions in the `src/__init__.py` script.
You should also try to use absolute imports whenever possible. Relative imports are
acceptable, but can create issues for projects where the directory structure is likely 
to change. See [PEP 328 for details on absolute imports](https://www.python.org/dev/peps/pep-0328/).