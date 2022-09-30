from typer.testing import CliRunner

from {{ cookiecutter.repo_name.replace('-', '_') }}.cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Hello, data science." in result.stdout
