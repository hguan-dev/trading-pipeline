import pytest
from pysrc.lasso_model import LassoModel


def test_buffer() -> None:
    model = LassoModel()

    for i in range(10):
        model.add_tick([(i, 1, True)])
        assert model.predict() is None

    for i in range(10):
        model.add_tick([(i, 1, True)])
        assert model.predict() is not None
