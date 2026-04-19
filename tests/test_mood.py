from app.brain.mood_engine import MoodEngine


def test_mood_has_current_state() -> None:
    assert "current_mood" in MoodEngine().get_state()
