from app.memory.conversation_store import ConversationStore
from app.memory.profile_store import ProfileStore


class MemoryManager:
    def __init__(self) -> None:
        self.conversations = ConversationStore()
        self.profile = ProfileStore()

    def remember_exchange(self, user_text: str, assistant_text: str) -> None:
        self.conversations.append({
            "user": user_text,
            "assistant": assistant_text,
        })

    def get_last_user_messages(self, limit: int = 5) -> list[str]:
        history = self.conversations.get_all()
        return [item["user"] for item in history[-limit:] if "user" in item]

    def get_last_answer(self) -> str | None:
        history = self.conversations.get_all()
        if not history:
            return None
        return history[-1].get("assistant")