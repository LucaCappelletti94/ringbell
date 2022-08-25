from ding import Ding
import pytest


def test_ding():
    d = Ding()
    with pytest.raises(ValueError):
        Ding(sample="kebab")
    with pytest.raises(ValueError):
        Ding(sample="kebab")
    with pytest.raises(ValueError):
        Ding(sample="tests/test_invalid_ding.py")
    Ding(sample=d._path)
