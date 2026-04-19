import json
from app.utils.paths import DATA_DIR


class ConversationStore:
    def __init__(self) -> None:
        self.path = DATA_DIR / "memory" / "short_term.json"
        self.data = self._load()

    def _load(self) -> list:
        try:
            with self.path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def read(self) -> list:
        return self.data

    def get_all(self) -> list:
        return self.data

    def append(self, item: dict) -> None:
        self.data.append(item)

        self.data = self.data[-20:]

        with self.path.open("w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=2)