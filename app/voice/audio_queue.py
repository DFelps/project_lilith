class AudioQueue:
    def __init__(self) -> None:
        self.items: list[str] = []

    def push(self, item: str) -> None:
        self.items.append(item)

    def pop(self) -> str | None:
        if not self.items:
            return None
        return self.items.pop(0)
