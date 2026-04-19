from pathlib import Path
from app.utils.paths import DATA_DIR


class KnowledgeStore:
    def __init__(self) -> None:
        self.base_path = DATA_DIR / "knowledge"

    def list_files(self) -> list[Path]:
        return [path for path in self.base_path.rglob("*") if path.is_file()]
