from ringbell import RingBell
import pytest


def test_ringbell():
    d = RingBell()
    with pytest.raises(ValueError):
        RingBell(sample="kebab")
    with pytest.raises(ValueError):
        RingBell(sample="kebab")
    with pytest.raises(ValueError):
        RingBell(sample="tests/test_invalid_RingBell.py")
    RingBell(sample=d._path)
