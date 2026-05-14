from typing import Any

from app.voice import f5_tts


def configure_tts(config: dict[str, Any] | None = None) -> None:
    return None


def get_provider_name() -> str:
    return "f5"


def is_available() -> bool:
    return f5_tts.is_available()


def warmup_tts() -> None:
    f5_tts.warmup_tts()


def generate_audio(text: str):
    return f5_tts.generate_audio(text)


def play_audio(wav: object, sample_rate: int = 24000) -> None:
    f5_tts.play_audio(wav, sample_rate)


def speak(text: str) -> str | None:
    return f5_tts.speak(text)
