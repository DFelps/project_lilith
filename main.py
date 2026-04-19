from app.core.orchestrator import LilithOrchestrator
from app.utils.config import load_app_config


def main() -> None:
    config = load_app_config()
    orchestrator = LilithOrchestrator(config)
    orchestrator.run_cli()


if __name__ == "__main__":
    main()
