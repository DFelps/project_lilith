from __future__ import annotations

import json
import time
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
STATE_PATH = BASE_DIR / "data" / "avatar" / "state.json"
VALID_STATES = {"idle", "thinking", "speaking"}


def set_avatar_state(state: str) -> None:
    if state not in VALID_STATES:
        return

    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "state": state,
        "updated_at": time.time(),
    }
    STATE_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def get_avatar_state() -> str:
    if not STATE_PATH.is_file():
        return "idle"

    try:
        payload = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return "idle"

    state = payload.get("state", "idle")
    return state if state in VALID_STATES else "idle"
