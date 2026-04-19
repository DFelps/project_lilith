from pathlib import Path
from app.memory.knowledge_store import KnowledgeStore


def main() -> None:
    store = KnowledgeStore()
    for file_path in store.list_files():
        print(file_path)


if __name__ == "__main__":
    main()
