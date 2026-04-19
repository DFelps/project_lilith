from app.memory.conversation_store import ConversationStore
from app.memory.profile_store import ProfileStore


class Retrieval:
    def __init__(self) -> None:
        self.conversations = ConversationStore()
        self.profile = ProfileStore()

    def build_context(self) -> str:
        profile = self.profile.read()
        history = self.conversations.read()[-5:]
        profile_text = f"Preferências do usuário: {profile}"
        history_text = "\n".join(
            f"Usuário: {item['user']}\nLilith: {item['assistant']}" for item in history
        )
        return f"{profile_text}\n\nHistórico recente:\n{history_text}".strip()
