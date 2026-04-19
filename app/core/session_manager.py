from datetime import datetime


class SessionManager:
    def __init__(self) -> None:
        self.session_started_at = datetime.now().isoformat()
