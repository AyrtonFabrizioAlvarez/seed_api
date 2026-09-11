import asyncio

import httpx

from src.interfaces.api.main import app


def test_health() -> None:
    async def make_request() -> httpx.Response:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            return await client.get("/health")

    response = asyncio.run(make_request())

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
