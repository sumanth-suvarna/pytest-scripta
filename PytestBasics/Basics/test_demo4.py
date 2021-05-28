import pytest


def test_a():
    assert True


@pytest.mark.skip(reason="testing skip")
def test_d():
    assert True


@pytest.mark.skip(reason="testing skip")
def test_c():
    assert True

