"""
Tests whether the releasenotes have been
generated correctly with whatsnew
"""
from whatsnew.core import get_git_news


def test_notes_generation(repo):
    """
    Tests a simple generation of releasenotes
    """
    # GIVEN & WHEN
    changelog = get_git_news(repository=repo)

    # THEN
    assert 'Signed-off-by' in changelog

