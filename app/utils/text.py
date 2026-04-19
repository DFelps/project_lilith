import re
from typing import List


def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_sentences(text: str) -> List[str]:
    parts = re.split(r"(?<=[.!?])\s+", normalize_spaces(text))
    return [part for part in parts if part]
