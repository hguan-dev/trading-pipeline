import pytest
from pysrc import intern  # type: ignore[attr-defined]


def test_pybind() -> None:
    assert intern.add(4, 5) == 9
