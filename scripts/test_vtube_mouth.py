import asyncio
from app.ui.vtube_studio import VTubeStudioClient


async def main():
    client = VTubeStudioClient()
    await client.connect()

    for value in [0.0, 0.2, 0.5, 0.8, 1.0, 0.0]:
        print("Enviando:", value)
        await client.set_mouth(value)
        await asyncio.sleep(1)

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())