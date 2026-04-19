from pathlib import Path
import uuid
import re
import asyncio

import sounddevice as sd
import soundfile as sf
from TTS.api import TTS
import torch

from app.voice.vtube_lipsync import play_with_lipsync


BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = BASE_DIR / "data" / "audio" / "generated"
REFERENCE_WAV = BASE_DIR / "data" / "voice" / "reference" / "lilith_reference.wav"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

_tts = None

TTS_CONFIG = {
    "language": "pt",
    "temperature": 0.3,
    "repetition_penalty": 1.2,
    "top_k": 30,
    "top_p": 0.85,
    "speed": 1.0,
}


def is_available() -> bool:
    return REFERENCE_WAV.is_file()


def get_tts() -> TTS:
    global _tts
    if _tts is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        _tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
        _tts.to(device)
    return _tts


def normalize_tts_text(text: str) -> str:
    text = text.strip()
    text = text.replace("...", " ")
    text = text.replace("…", " ")
    text = text.replace("\n", " ")
    text = text.replace("—", " ")
    text = text.replace("–", " ")
    text = re.sub(r"[.]+", " ", text)
    text = re.sub(r"[,;:!?]+", " ", text)
    text = text.replace('"', "")
    text = text.replace("'", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def generate_audio(text: str) -> tuple[str, object] | None:
    if not text or not text.strip():
        return None

    if not is_available():
        return None

    normalized_text = normalize_tts_text(text)
    output_path = OUTPUT_DIR / f"{uuid.uuid4()}.wav"

    tts = get_tts()

    with torch.no_grad():
        wav = tts.tts(
            text=normalized_text,
            speaker_wav=str(REFERENCE_WAV),
            **TTS_CONFIG,
        )

    wav = torch.as_tensor(wav).detach().cpu().numpy().astype("float32")

    sf.write(str(output_path), wav, 24000)
    return str(output_path), wav


def play_audio(wav: object) -> None:
    sd.stop()
    sd.play(wav, 24000)
    sd.wait()


def speak(text: str) -> str | None:
    generated = generate_audio(text)
    if not generated:
        return None

    output_path, wav = generated
    asyncio.run(play_with_lipsync(wav, 24000))
    #sf.write(str(output_path), wav, 24000)
    return output_path
    