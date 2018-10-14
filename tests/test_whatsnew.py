"""
Tests whether the releasenotes have been
generated correctly with whatsnew
"""
from whatsnew.core import get_git_news


def test_notes_generation(repo):
    """
    Tests a simple generation of releasenotes
    """
    # GIVEN
    repo.create_commit("Initial commit", tag="v0.0.0")
    repo.create_commit("Release version 1.0.0", tag="v1.0.0")
    repo.create_commit("Old changelog", signoff=True)
    repo.create_commit("Release version 2.0.0", tag="v2.0.0", signoff=True)
    repo.create_commit("This is a change")
    repo.create_commit("In changelog", signoff=True)

    # WHEN
    changelog = get_git_news(repository=str(repo.path))

    # THEN
    assert 'In changelog' in changelog

