from pathlib import Path
import yaml

from app.utils.paths import CONFIG_DIR


def _load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}
    return data


def load_app_config() -> dict:
    return {
        "app": _load_yaml(CONFIG_DIR / "app.yaml"),
        "models": _load_yaml(CONFIG_DIR / "models.yaml"),
        "voice": _load_yaml(CONFIG_DIR / "voice.yaml"),
        "vision": _load_yaml(CONFIG_DIR / "vision.yaml"),
        "privacy": _load_yaml(CONFIG_DIR / "privacy.yaml"),
    }
