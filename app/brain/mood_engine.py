import json
from app.utils.paths import DATA_DIR


class MoodEngine:
    def __init__(self) -> None:
        self.path = DATA_DIR / "brain" / "mood.json"

    def get_state(self) -> dict:
        with self.path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def set_mood(self, mood: str) -> dict:
        state = self.get_state()
        state["current_mood"] = mood
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(state, file, ensure_ascii=False, indent=2)
        return state
