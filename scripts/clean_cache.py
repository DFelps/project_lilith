from pathlib import Path
from app.utils.paths import DATA_DIR


def clean_generated_audio() -> None:
    target = DATA_DIR / "audio" / "generated"
    for path in target.glob("*"):
        if path.is_file():
            path.unlink()


if __name__ == "__main__":
    clean_generated_audio()
    print("Cache limpo.")
