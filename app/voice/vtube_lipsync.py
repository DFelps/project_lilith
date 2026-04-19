import asyncio
import numpy as np
import sounddevice as sd

from app.ui.vtube_studio import VTubeStudioClient


SAMPLE_RATE = 24000


def chunk_audio(wav: np.ndarray, sample_rate: int, chunk_ms: int = 30):
    chunk_size = int(sample_rate * (chunk_ms / 1000))
    for i in range(0, len(wav), chunk_size):
        yield wav[i:i + chunk_size]


def compute_mouth_value(chunk: np.ndarray) -> float:
    if len(chunk) == 0:
        return 0.0

    peak = float(np.max(np.abs(chunk)))
    rms = float(np.sqrt(np.mean(np.square(chunk))))
    value = max(peak * 0.9, rms * 2.2)

    return max(0.0, min(1.0, value))


async def play_with_lipsync(wav: object, sample_rate: int = SAMPLE_RATE) -> None:
    wav = np.asarray(wav, dtype=np.float32)

    if wav.ndim > 1:
        wav = wav.mean(axis=1)

    client = VTubeStudioClient()
    await client.connect()

    sd.stop()
    sd.play(wav, sample_rate)

    chunk_ms = 30
    sleep_time = chunk_ms / 1000

    for chunk in chunk_audio(wav, sample_rate, chunk_ms=chunk_ms):
        mouth_value = compute_mouth_value(chunk)
        await client.set_mouth(mouth_value)
        await asyncio.sleep(sleep_time)

    sd.wait()
    await client.set_mouth(0.0)
    await client.close()