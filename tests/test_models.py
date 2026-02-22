from __future__ import annotations

import models


def test_user_and_library_item_creation():
    user = models.User(name="Ada Lovelace", email="ada@example.com")
    item = models.LibraryItem(
        title="Analytical Engine Notes",
        media_type="document",
        file_path="/library/notes.pdf",
        owner=user,
    )

    assert user.name == "Ada Lovelace"
    assert user.email == "ada@example.com"
    assert item.title == "Analytical Engine Notes"
    assert item.media_type == "document"
    assert item.file_path == "/library/notes.pdf"
    assert item.owner is user
