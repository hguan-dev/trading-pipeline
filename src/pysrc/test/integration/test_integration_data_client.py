# tests/integration/test_data_client.py

import pytest
from pysrc.data_client import DataClient, Trade, Side


@pytest.mark.integration
def test_data_client_integration() -> None:
    """
    Integration test for DataClient to fetch and parse data from Gemini API.
    """

    client = DataClient()

    try:
        data = client.get_data()
    except Exception as e:
        pytest.fail(f"DataClient integration test failed with error: {e}")

    assert isinstance(data, list), "get_data should return a list"
    assert len(data) > 0, "No trades were returned from the API"

    first_trade = data[0]
    assert "timestampms" in first_trade, "Missing 'timestampms' in parsed trade"
    assert "id" in first_trade, "Missing 'id' in parsed trade"
    assert "price" in first_trade, "Missing 'price' in parsed trade"
    assert "volume" in first_trade, "Missing 'volume' in parsed trade"
    assert "side" in first_trade, "Missing 'side' in parsed trade"

    assert isinstance(first_trade["timestampms"], int), "timestampms should be an int"
    assert isinstance(first_trade["id"], int), "id should be an int"
    assert isinstance(first_trade["price"], float), "price should be a float"
    assert isinstance(first_trade["volume"], float), "volume should be a float"
    assert isinstance(first_trade["side"], Side), "side should be a Side enum"

    print(f"First trade data: {first_trade}")
