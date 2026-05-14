import os
from typing import Any

_provider_name = os.getenv("LILITH_TTS_PROVIDER", "f5").strip().lower()
_provider_module = None


def configure_tts(config: dict[str, Any] | None = None) -> None:
    global _provider_name, _provider_module

    tts_config = (config or {}).get("tts", {})
    provider = tts_config.get("provider") or os.getenv("LILITH_TTS_PROVIDER") or _provider_name
    provider = str(provider).strip().lower()

    if provider not in {"f5", "xtts"}:
        print(f"[TTS] provider inválido '{provider}', usando f5")
        provider = "f5"

    if provider != _provider_name:
        _provider_module = None

    _provider_name = provider


def get_provider_name() -> str:
    return _provider_name


def get_provider():
    global _provider_module

    if _provider_module is not None:
        return _provider_module

    if _provider_name == "xtts":
        from app.voice import xtts_tts as provider
    else:
        from app.voice import f5_tts as provider

    _provider_module = provider
    print(f"[TTS] provider ativo: {_provider_name}")

    return _provider_module


def is_available() -> bool:
    return get_provider().is_available()


def warmup_tts() -> None:
    get_provider().warmup_tts()


def generate_audio(text: str):
    return get_provider().generate_audio(text)


def play_audio(wav: object, sample_rate: int = 24000) -> None:
    get_provider().play_audio(wav, sample_rate)


def speak(text: str) -> str | None:
    return get_provider().speak(text)
