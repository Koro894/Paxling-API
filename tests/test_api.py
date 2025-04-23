import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app

@pytest.mark.asyncio
async def test_get_books():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test",) as ac:
        await ac.get("http://localhost:8010/")
