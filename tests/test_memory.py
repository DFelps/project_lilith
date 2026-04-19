from app.memory.profile_store import ProfileStore


def test_profile_store() -> None:
    assert "preferred_language" in ProfileStore().read()
