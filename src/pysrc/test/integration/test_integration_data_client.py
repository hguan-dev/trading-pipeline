# tests/integration/test_data_client.py

import pytest
from pysrc.data_client import DataClient, Side


@pytest.mark.integration
def test_data_client_integration() -> None:
    """
    Integration test for DataClient to fetch and parse data from Gemini API.
    """

    client = DataClient()

    data = client.get_data()

    assert isinstance(data, list)
    assert len(data) > 0

    first_trade = data[0]
    assert "timestampms" in first_trade
    assert "id" in first_trade
    assert "price" in first_trade
    assert "volume" in first_trade
    assert "side" in first_trade

    assert isinstance(first_trade["timestampms"], int)
    assert isinstance(first_trade["id"], int)
    assert isinstance(first_trade["price"], float)
    assert isinstance(first_trade["volume"], float)
    assert isinstance(first_trade["side"], Side)

    print(f"First trade data: {first_trade}")
