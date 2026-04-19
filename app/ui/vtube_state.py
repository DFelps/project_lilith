import asyncio

from app.ui.vtube_studio import VTubeStudioClient


def set_vtube_state(state: str) -> None:
    async def runner():
        client = VTubeStudioClient()
        await client.connect()
        await client.set_state(state)
        await client.close()

    asyncio.run(runner())