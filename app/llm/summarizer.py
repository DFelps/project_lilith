class Summarizer:
    def trim(self, text: str, max_chars: int = 900) -> str:
        if len(text) <= max_chars:
            return text
        return text[: max_chars - 3].rstrip() + "..."
