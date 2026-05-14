import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
REPLACEMENTS_PATH = BASE_DIR / "data" / "voice" / "normalizer" / "replacements.json"


DEFAULT_REPLACEMENTS = {
    "CPU": "C P U",
    "GPU": "G P U",
    "SSD": "S S D",
    "System32": "System trinta e dois",
    "Windows": "Uíndous",
    "Docker": "Dóquer",
    "R$": " reais ",
    "%": " por cento ",
    "+": " mais ",
    "=": " igual a ",
    "/": " dividido por ",
}


def load_replacements() -> dict:
    if REPLACEMENTS_PATH.is_file():
        with REPLACEMENTS_PATH.open("r", encoding="utf-8") as file:
            return {**DEFAULT_REPLACEMENTS, **json.load(file)}
    return DEFAULT_REPLACEMENTS


def make_tts_friendly(text: str) -> str:
    replacements = load_replacements()

    for old, new in sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(old, new)

    text = re.sub(r"\b(\d+)\s*\+\s*(\d+)\b", r"\1 mais \2", text)
    text = re.sub(r"\b(\d+)\s*-\s*(\d+)\b", r"\1 menos \2", text)
    text = re.sub(r"\b(\d+)\s*/\s*(\d+)\b", r"\1 dividido por \2", text)
    text = re.sub(r"\b(\d+)\s*x\s*(\d+)\b", r"\1 vezes \2", text, flags=re.IGNORECASE)

    text = re.sub(r"\s+", " ", text)
    return text.strip()