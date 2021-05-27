import pytest


@pytest.fixture
def order():
    print("Executing Order Fixture")
    return []


@pytest.fixture
def order1():
    print("Executing Order1 Fixture")


@pytest.fixture
def append_first(order):
    print("Executing append_first Fixture")
    order.append(1)


@pytest.fixture
def append_second(order, append_first):
    print("Executing append_second Fixture")
    order.extend([2])


@pytest.fixture(autouse=True)
def append_third(order, append_second):
    print("Executing append_third autouse Fixture")
    order += [3]


def test_order(order):
    assert order == [1, 2]