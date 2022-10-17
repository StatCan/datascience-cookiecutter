"""Test building the project."""

import re

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

    # Setup and TOML files needs to exist
    assert result.project_path.joinpath('setup.cfg').exists()
    assert result.project_path.joinpath('pyproject.toml').exists()


@pytest.mark.parametrize("inp_using_r", ["No", "Yes"])
def test_project_version(cookies, inp_using_r: str) -> None:
    """Ensure that the project version is properly set."""
    vnum = "1.0.0"
    vfile = "version"
    result = cookies.bake(
        extra_context={
            "project_version": vnum,
            "using_R": inp_using_r
        })
    
    # This should have created a version file with our version number
    assert result.project_path.joinpath(vfile).exists()
    assert result.project_path.joinpath(vfile).is_file()

    contents = result.project_path.joinpath(vfile).read_text()
    assert contents == vnum
