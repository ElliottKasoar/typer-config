"""Test Simple YAML Example."""

from __future__ import annotations

import typer
from typer.testing import CliRunner
from typing_extensions import Annotated

from typer_config.decorators import use_yaml_config


class _CustomClass:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return f"<CustomClass: value={self.value}>"


def _parse_custom_class(value: str):
    return _CustomClass(value * 2)


RUNNER = CliRunner()
CustomType = Annotated[_CustomClass, typer.Argument(parser=_parse_custom_class)]


def test_simple_example_decorated():
    """Test YAML app with custom type and decorators."""

    app = typer.Typer()

    @app.command()
    @use_yaml_config()
    def main(
        arg1: CustomType = 1,
    ):
        typer.echo(f"{arg1}")

    result = RUNNER.invoke(app, ["--help"])
    assert result.exit_code == 0
