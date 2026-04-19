class Safety:
    def validate(self, user_text: str) -> str:
        blocked = ["execute", "rode esse comando", "apague arquivo", "delete everything"]
        lowered = user_text.lower()
        if any(pattern in lowered for pattern in blocked):
            return "Posso orientar de forma segura e geral, mas não vou executar nem instruir ações destrutivas."
        return ""
