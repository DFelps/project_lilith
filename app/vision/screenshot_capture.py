from pathlib import Path
from datetime import datetime
from app.utils.paths import DATA_DIR


class ScreenshotCapture:
    def reserve_path(self) -> Path:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        return DATA_DIR / "vision" / "screenshots" / f"shot_{ts}.png"
