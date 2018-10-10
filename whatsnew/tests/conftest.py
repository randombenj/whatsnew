import uuid
import shutil
import tempfile
from pathlib import Path

import pytest
from git import Repo


@pytest.fixture
def repo():
    """
    Creates a fake git repository
    """
    repo_path = Path(tempfile.mkdtemp())
    git_repo = Repo.init(str(repo_path)).git

    def create_commit(tag=None, signoff=False):
        new_file = repo_path / str(uuid.uuid4())
        new_file.touch()  # create the file
        git_repo.add(new_file.name)
        if signoff:
            signoff = "\n\nSigned-off-by: John Snow <john.snow@got.invalid>"

        git_repo.commit(
            "-m",
            "Add file {}{}".format(new_file.name, signoff),
            author="John Snow <john.snow@got.invalid>"
        )

        if tag:
            git_repo.tag(
                tag,
                message="Created tag '{}'".format(tag)
            )

    create_commit(tag="v0.0.0")
    create_commit(tag="v1.0.0")
    create_commit(signoff=True)
    create_commit(tag="v2.0.0", signoff=True)
    create_commit()
    create_commit(signoff=True)

    yield str(repo_path)
    # clean up the git repo
    shutil.rmtree(str(repo_path))
