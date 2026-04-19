from app.llm.summarizer import Summarizer
from app.utils.text import split_sentences


class ResponseBuilder:
    def __init__(self) -> None:
        self.summarizer = Summarizer()

    def build(self, text: str) -> dict:
        cleaned = self.summarizer.trim(text)
        return {
            "text": cleaned,
            "sentences": split_sentences(cleaned),
        }
