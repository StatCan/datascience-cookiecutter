from pathlib import Path

from sphinx.cmd.build import main


def test_docs_build(tmp_path: Path) -> None:
    """Check that our own documentation builds correctly."""
    assert main(["-b", "html", "docs", str(tmp_path.joinpath("_build"))]) == 0