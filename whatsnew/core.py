"""
Create releasenotes from the git hitory
"""
import subprocess

import git


def create_notes(version, from_version="", repository=".", gitlog_format=None):
    """
    Creates releasenotes from the git history
    """
    git_news = get_git_news(from_version, repository, gitlog_format)
    print(git_news)


def get_git_news(from_version="", repository=".", gitlog_format=None):
    """
    Gets the git news of a repository in the history

    Args:
     from_version (str): Version in the git history e.g. v1.0.0 or v1.0.0..v2.0.0
     repository (str): Path to the git repository
     gitlog_format (str): How to format the git log
    """
    # set default values
    if not gitlog_format:
        gitlog_format = "%n - **%s** %n%n%w(74,3,3)%b"

    repo = git.Git(repository)

    if not from_version:
        # get the last version if we don't know
        # from where to generate the changelog
        from_version = repo.describe(
            "--tags",
            "--abbrev=0"
        )

    if ".." not in from_version:
        # create the changelog to the current HEAD
        # when no different information is given
        from_version = from_version + "..HEAD"

    return repo.log(
        from_version,
        "--grep",
        "Signed-off-by",
        "--pretty=format:{}".format(gitlog_format)
    )
