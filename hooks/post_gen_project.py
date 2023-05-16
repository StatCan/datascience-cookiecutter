"""
Post project generation hook.

Removes files that don't make sense based on user choices.
"""

import shutil
from pathlib import Path


# Files to be completely removed
REMOVE_PATHS = [
    '{% if cookiecutter.using_R == "Yes" %} setup.cfg {% endif %}',
    '{% if cookiecutter.using_R == "Yes" %} pyproject.toml {% endif %}',
    '{% if cookiecutter.using_R == "Yes" %} tests/test_api.py {% endif %}',
    '{% if cookiecutter.using_R == "Yes" %} tests/test_cli.py {% endif %}',
    '{% if cookiecutter.using_R == "No" %} tests/testthat {% endif %}',
    '{% if cookiecutter.using_R == "Yes" %} src/{{ cookiecutter.__pypkg }} {% endif %}',
    '{% if cookiecutter.VCS != "Gitlab" %} .gitlab-ci.yml {% endif %}',
]

for item in REMOVE_PATHS:
    item = item.strip()
    if not item:
        continue
    item = Path(item)
    if item.exists():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
