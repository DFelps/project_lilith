class Router:
    def classify(self, text: str) -> str:
        lowered = text.lower()
        if any(keyword in lowered for keyword in ["print", "tela", "imagem", "screenshot"]):
            return "vision"
        if any(keyword in lowered for keyword in ["código", "codigo", "função", "funcao", "erro"]):
            return "light_technical"
        return "general"
