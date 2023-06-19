"""Test building the project."""

import os
import re
import subprocess

import pytest
from sphinx.cmd.build import main

@pytest.mark.parametrize("inp_en_name", ["a", "b"])
@pytest.mark.parametrize("inp_fr_name", ["x", "y"])
@pytest.mark.parametrize("inp_using_r", ["No", "Yes"])
def test_repo_dir_correct(
    cookies,
    inp_en_name: str,
    inp_fr_name: str,
    inp_using_r: str
) -> None:
    """Check that the project builds correctly."""
    result = cookies.bake(
        extra_context={
            "project_name_en": inp_en_name,
            "project_name_fr": inp_fr_name,
            "using_R": inp_using_r
        })
    
    # Ensure things built without exceptions
    assert result.exit_code == 0
    assert result.exception is None

    # The generated project directory should reflect the project name
    assert result.project_path.name == inp_en_name
    assert result.project_path.is_dir()


@pytest.mark.parametrize("inp_using_r", ["No", "Yes"])
def test_builds_correctly(cookies, inp_using_r: str) -> None:
    """Check that the project builds correctly."""
    result = cookies.bake(extra_context={"using_R": inp_using_r})
    
    # Ensure things built without exceptions
    assert result.exit_code == 0
    assert result.exception is None

    # There should be no `cookiecutter.variable_name` entries in any file
    all_files = [f for f in result.project_path.rglob("*") if f.is_file()]
    for result_file in all_files:
        try:
            with result_file.open(encoding="utf-8") as f:
                assert re.search(r"{+ ?cookiecutter\.\w+ ?}+", f.read()) is None
        except UnicodeDecodeError:
            continue
    
    # Check that the docs build as expected
    docs_dir = result.project_path.joinpath("docs")
    assert (main(["-b", "html", str(docs_dir), str(docs_dir.joinpath("_build"))])) == 0


@pytest.mark.parametrize("inp_using_r", ["No", "Yes"])
def test_oss_template(cookies, inp_using_r: str) -> None:
    """Ensure the minimum OSS office template files are present."""
    result = cookies.bake(extra_context={"using_R": inp_using_r})

    # Check each of the expected files
    assert result.project_path.joinpath('LICENSE').exists()
    assert result.project_path.joinpath('README.md').exists()
    assert result.project_path.joinpath('SECURITY.md').exists()
    assert result.project_path.joinpath('CONTRIBUTING.md').exists()


@pytest.mark.parametrize("inp_using_r", ["No", "Yes"])
def test_is_py_pkg(cookies, inp_using_r: str) -> None:
    """Check that the generated project is a python package."""
    result = cookies.bake(extra_context={"using_R": inp_using_r})

    # Code should be in a src directory
    assert result.project_path.joinpath('src').exists()

    # Setup and TOML files needs to exist for Python only
    if inp_using_r == "No":
        assert result.project_path.joinpath('pyproject.toml').exists()


@pytest.mark.parametrize("environment", ["conda", "venv"])
def test_target_env(cookies, environment: str) -> None:
    """Validate conda support renders appropriately."""
    result = cookies.bake(extra_context={"environment": environment})

    # For conda environments there should be some stubbed files
    conda_envs_found = result.project_path.joinpath("conda-envs").exists()
    conda_env_stub = result.project_path.joinpath("environment.yml").exists()
    if environment == "conda":
        assert conda_envs_found == True
        assert conda_env_stub == True
    else:
        assert conda_envs_found == False
        assert conda_env_stub == False


# @pytest.mark.skip("Raises py.error.EBUSY error when trying to clean up test files")
def test_pypkg_build(cookies):
    """Try building the resulting python package."""
    result = cookies.bake(extra_context={"using_R": "No"})
    assert result.project_path.is_dir()

    # Change to the baked project and try to execute a build
    os.chdir(result.project_path)
    # Python uses SCM for version numbering, so init a repo
    subprocess.run(["git", "init", "-b", "main", "."])
    subprocess.run(["git", "add", "-A"])
    subprocess.run(["git", "commit", "-m", "'Initialize'"])
    # Try to build the package
    completed = subprocess.run(["python", "-m", "build"])
    assert completed.returncode == 0
