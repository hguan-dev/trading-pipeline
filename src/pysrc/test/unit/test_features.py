import pytest
from pysrc import intern # type:ignore
import math

# Test data
trade_data = [
    (100.5, 10, True),   # Price, Volume, Buy
    (101.0, 5, False),   # Price, Volume, Sell
    (102.0, 20, True),   # Price, Volume, Buy
]

def test_add() -> None:
    """Test the add function."""
    assert intern.add(4, 5) == 9

def test_ntrades_feature() -> None:
    """Test NTradesFeature compute_feature."""
    feature = intern.NTradesFeature()
    result = feature.compute_feature(trade_data)
    assert result == len(trade_data)

def test_percent_buy_feature() -> None:
    """Test PercentBuyFeature compute_feature."""
    feature = intern.PercentBuyFeature()
    result = feature.compute_feature(trade_data)
    assert math.isclose(result, 2/3, rel_tol=1e-6) 

def test_percent_sell_feature() -> None:
    """Test PercentSellFeature compute_feature."""
    feature = intern.PercentSellFeature()
    result = feature.compute_feature(trade_data)
    assert math.isclose(result, 1/3, rel_tol=1e-6) 

def test_five_tick_volume_feature() -> None:
    """Test FiveTickVolumeFeature compute_feature."""
    feature = intern.FiveTickVolumeFeature()
    tick_data = [trade_data] * 5  # Simulate 5 ticks of data
    result = 0.0
    for tick in tick_data:
        result = feature.compute_feature(tick)
    expected_volume = sum(trade[1] for trade in trade_data) * 5
    assert result == expected_volume

