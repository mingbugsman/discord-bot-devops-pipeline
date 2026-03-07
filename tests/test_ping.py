import pytest
from unittest.mock import AsyncMock, MagicMock
from bot import ping

@pytest.mark.asyncio
async def test_ping():
    ctx = MagicMock()
    ctx.send = AsyncMock()

    await ping(ctx)

    ctx.send.assert_called_once_with("Hallo hallo hallo!")