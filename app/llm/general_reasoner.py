from app.llm.ollama_client import OllamaClient
from app.llm.prompts import build_system_prompt


class GeneralReasoner:
    def __init__(self, persona: dict, model: str) -> None:
        self.persona = persona
        self.client = OllamaClient(model=model)

    def answer(self, user_text: str, context: str = "") -> str:
        prompt = user_text
        if context:
            prompt = f"Contexto útil:\n{context}\n\nPergunta do usuário:\n{user_text}"
        system_prompt = build_system_prompt(self.persona)
        return self.client.generate(system_prompt=system_prompt, user_prompt=prompt)

    def stream_answer(self, user_text: str, context: str = ""):
        prompt = user_text
        if context:
            prompt = f"Contexto útil:\n{context}\n\nPergunta do usuário:\n{user_text}"
        system_prompt = build_system_prompt(self.persona)
        yield from self.client.stream_generate(system_prompt=system_prompt, user_prompt=prompt)