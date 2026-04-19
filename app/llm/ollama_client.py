import json
import os

import requests


class OllamaClient:
    def __init__(self, host: str | None = None, model: str = "llama3.1:8b") -> None:
        self.host = host or os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
        self.model = model

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        response = requests.post(
            f"{self.host}/api/chat",
            json={
                "model": self.model,
                "stream": False,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            },
            timeout=120,
        )
        response.raise_for_status()
        payload = response.json()
        return payload.get("message", {}).get("content", "Não consegui responder agora.")

    def stream_generate(self, system_prompt: str, user_prompt: str):
        with requests.post(
            f"{self.host}/api/chat",
            json={
                "model": self.model,
                "stream": True,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            },
            timeout=120,
            stream=True,
        ) as response:
            response.raise_for_status()

            for line in response.iter_lines(decode_unicode=True):
                if not line:
                    continue

                payload = json.loads(line)
                message = payload.get("message", {}).get("content", "")

                if message:
                    yield message

                if payload.get("done"):
                    break