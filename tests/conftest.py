import uuid
import shutil
import tempfile
from pathlib import Path

import pytest
from git import Repo


class GitRepoFixture():
    def __init__(self, repo_path):
        self._repo_path = repo_path
        self._git_repo = Repo.init(str(self._repo_path)).git
        self._git_repo.config("user.name", "John Snow")
        self._git_repo.config("user.email", "john.snow@got.invalid")


    @property
    def path(self):
        return self._repo_path


    def create_commit(self, message, tag=None, signoff=False):
        new_file = self._repo_path / str(uuid.uuid4())
        new_file.touch()  # create the file
        self._git_repo.add(new_file.name)
        if signoff:
            signoff = "\n\nSigned-off-by: John Snow <john.snow@got.invalid>"

        self._git_repo.commit(
            "-m",
            "{}\n\nAdd file {}{}".format(message, new_file.name, signoff),
            author="John Snow <john.snow@got.invalid>"
        )

        if tag:
            self._git_repo.tag(
                tag,
                message="Created tag '{}'".format(tag)
            )


@pytest.fixture
def repo():
    """
    Creates a fake git repository
    """
    repo_path = Path(tempfile.mkdtemp())
    yield GitRepoFixture(repo_path)
    # clean up the git repo
    shutil.rmtree(str(repo_path))
