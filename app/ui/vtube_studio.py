import json
import uuid
from pathlib import Path

import websockets


class VTubeStudioClient:
    def __init__(self, host: str = "127.0.0.1", port: int = 8001) -> None:
        self.url = f"ws://{host}:{port}"
        self.ws = None
        self.plugin_name = "Lilith"
        self.plugin_developer = "Daniel"
        self.token_path = Path("data/vtube_token.txt")
        self.authentication_token = None
        self.mouth_parameter_id = "LilithMouthOpen"

    async def connect(self) -> None:
        self.ws = await websockets.connect(self.url)

        if self.token_path.exists():
            self.authentication_token = self.token_path.read_text(encoding="utf-8").strip()

        if not self.authentication_token:
            await self._request_auth_token()
            self.token_path.parent.mkdir(parents=True, exist_ok=True)
            self.token_path.write_text(self.authentication_token, encoding="utf-8")

        await self._authenticate()
        await self.ensure_mouth_parameter()

    async def close(self) -> None:
        if self.ws:
            await self.ws.close()

    async def _send(self, message_type: str, data: dict) -> dict:
        payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": str(uuid.uuid4()),
            "messageType": message_type,
            "data": data,
        }
        await self.ws.send(json.dumps(payload))
        response = await self.ws.recv()
        return json.loads(response)

    async def _request_auth_token(self) -> None:
        response = await self._send(
            "AuthenticationTokenRequest",
            {
                "pluginName": self.plugin_name,
                "pluginDeveloper": self.plugin_developer,
            },
        )

        if response.get("messageType") == "APIError":
            raise RuntimeError(f"Erro ao pedir token: {response}")

        self.authentication_token = response["data"]["authenticationToken"]

    async def _authenticate(self) -> None:
        response = await self._send(
            "AuthenticationRequest",
            {
                "pluginName": self.plugin_name,
                "pluginDeveloper": self.plugin_developer,
                "authenticationToken": self.authentication_token,
            },
        )

        if response.get("messageType") == "APIError":
            raise RuntimeError(f"Erro ao autenticar plugin: {response}")

    async def ensure_mouth_parameter(self) -> None:
        response = await self._send(
            "ParameterCreationRequest",
            {
                "parameterName": self.mouth_parameter_id,
                "explanation": "Custom mouth open parameter for Lilith lip sync",
                "min": 0.0,
                "max": 1.0,
                "defaultValue": 0.0,
            },
        )

        if response.get("messageType") not in {"ParameterCreationResponse", "APIError"}:
            raise RuntimeError(f"Resposta inesperada ao criar parâmetro: {response}")

        if response.get("messageType") == "APIError":
            error_id = response.get("data", {}).get("errorID")
            if error_id not in {50, 51, 352}:
                raise RuntimeError(f"Erro ao criar parâmetro: {response}")

    async def set_mouth(self, value: float) -> None:
        value = max(0.0, min(1.0, value))
        response = await self._send(
            "InjectParameterDataRequest",
            {
                "faceFound": True,
                "mode": "set",
                "parameterValues": [
                    {
                        "id": self.mouth_parameter_id,
                        "value": value,
                    }
                ],
            },
        )

        if response.get("messageType") == "APIError":
            raise RuntimeError(f"Erro ao injetar parâmetro: {response}")

    async def trigger_hotkey(self, hotkey_name: str) -> None:
        response = await self._send(
            "HotkeyTriggerRequest",
            {
                "hotkeyID": hotkey_name,
            },
        )

        if response.get("messageType") == "APIError":
            raise RuntimeError(f"Erro ao disparar hotkey '{hotkey_name}': {response}")

    async def set_state(self, state: str) -> None:
        mapping = {
            "idle": "My Animation 1",
            "thinking": "thinking_1",
            "speaking": "My Animation 2",
        }

        hotkey_name = mapping.get(state)
        if not hotkey_name:
            return

        await self.trigger_hotkey(hotkey_name)