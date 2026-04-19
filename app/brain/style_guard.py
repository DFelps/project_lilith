class StyleGuard:
    def enforce(self, text: str) -> str:
        banned_patterns = [
            "aqui está o sistema inteiro",
            "segue a implementação completa",
            "copie e cole este código gigante",
        ]
        lowered = text.lower()
        for pattern in banned_patterns:
            if pattern in lowered:
                return "Posso explicar por alto e resumir a ideia geral, mas sem despejar uma implementação inteira."
        return text
