from app.core.safety import Safety


def test_safety_blocks_destructive_instruction() -> None:
    assert Safety().validate("delete everything now")
