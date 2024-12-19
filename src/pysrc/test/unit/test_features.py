import pytest
from pysrc import intern  # type:ignore
import math

# Test data
trade_data = [
    (100.5, 10, True),  # Price, Volume, Buy
    (101.0, 5, False),  # Price, Volume, Sell
    (102.0, 20, True),  # Price, Volume, Buy
]


def test_add() -> None:
    """Test the add function."""
    assert intern.add(4, 5) == 9


def test_ntrades_feature() -> None:
    feature = intern.NTradesFeature()
    result = feature.compute_feature(trade_data)
    assert result == len(trade_data)


def test_percent_buy_feature() -> None:
    feature = intern.PercentBuyFeature()
    result = feature.compute_feature(trade_data)
    assert math.isclose(result, 2 / 3, rel_tol=1e-6)


def test_percent_sell_feature() -> None:
    feature = intern.PercentSellFeature()
    result = feature.compute_feature(trade_data)
    assert math.isclose(result, 1 / 3, rel_tol=1e-6)


def test_five_tick_volume_feature() -> None:
    feature = intern.FiveTickVolumeFeature()
    tick_data = [
        [(2, 1, False)],
        [(1, 1, False)],
        [(1, 1, False), (1, 1, True)],
        [(1, 1, False), (1, 1, True)],
        [(2, 1, False), (1, 1, True)],
        [(1, 1, False), (1, 1, True)],
        [(2, 1, False), (1, 1, True)],
    ]

    expected_results = [1.0, 2.0, 4.0, 6.0, 8.0, 9.0, 10.0]

    for tick, expected in zip(tick_data, expected_results):
        result = feature.compute_feature(tick)
        assert result == expected
