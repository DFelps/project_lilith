def is_repeated_question(current: str, history: list[str]) -> bool:
    current = current.lower().strip()
    return any(current == h.lower().strip() for h in history[-5:])


AGGRESSIVE_WORDS = [
    "idiota", "burro", "lixo", "merda", "foda-se",
    "vai se", "otario", "otária", "fdp"
]


def is_aggressive(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in AGGRESSIVE_WORDS)