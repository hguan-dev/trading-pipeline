import pytest
from pysrc import intern

def test() -> None:
    assert intern.add(4, 2) == 6
