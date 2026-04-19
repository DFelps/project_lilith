from app.core.router import Router


def test_router_general() -> None:
    assert Router().classify("me explica a lua") == "general"
