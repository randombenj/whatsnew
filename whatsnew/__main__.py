"""
Commandline interface for whatsnew
"""

import click

from .core import create_notes


@click.command()
@click.argument("version")
@click.argument("repository", required=False, type=click.Path())
@click.option(
    "-f",
    "--from-version",
    help="Where in the git history the notes should be created from. Examples: v1.0.0, v1.0.0..v2.0.0"
)
@click.option(
    "-g",
    "--gitlog-format",
    help="Specify how the gitlog should be formated. Default: '%n - **%s** %n%n%w(74,3,3)%b'"
)
@click.option(
    "-s",
    "--only-signed-off",
    help="Use only signed off commits (git commit -s) to generate notes"
)
def cli(version, from_version, repository, gitlog_format, only_signed_off):
    """
    Create releasenotes from your git history
    """
    create_notes(version, from_version, repository, gitlog_format)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
