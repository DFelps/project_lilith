import json
from pathlib import Path

from app.utils.paths import DATA_DIR


class PersonaLoader:
    def __init__(self) -> None:
        self.persona_path = DATA_DIR / "brain" / "persona.json"

    def load(self) -> dict:
        with self.persona_path.open("r", encoding="utf-8") as file:
            return json.load(file)
