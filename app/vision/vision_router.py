class VisionRouter:
    def choose_mode(self, user_text: str) -> str:
        lowered = user_text.lower()
        if "texto" in lowered or "ocr" in lowered:
            return "ocr"
        return "vision"
