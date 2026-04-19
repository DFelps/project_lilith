import json
from app.utils.paths import DATA_DIR


class ProfileStore:
    def __init__(self) -> None:
        self.path = DATA_DIR / "memory" / "profile.json"

    def read(self) -> dict:
        with self.path.open("r", encoding="utf-8") as file:
            return json.load(file)
