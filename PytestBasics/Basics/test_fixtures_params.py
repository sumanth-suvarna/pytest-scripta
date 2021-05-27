import pytest


@pytest.fixture(params=["apple", "mango", "banana"], scope="class")
def fruits(request):
    print("Executing Fixture - Class")
    request.cls.fruits = request.param
    yield request.param
    print("Terminating Fixture - Class")


@pytest.fixture(params=["apple", "mango", "banana"], scope="module")
def fruit(request):
    print("Executing Fixture - Module")
    yield request.param
    print("Terminating Fixture - Module")


def test_small_fruit(fruit):
    print(f"Small fruit is: {fruit}")
    assert True


# @pytest.mark.depends(on=["test_large_fruit"])
def test_medium_fruit(fruit):
    print(f"Medium fruit is: {fruit}")
    assert True


def test_large_fruit(fruit):
    print(f"Large fruit is: {fruit}")
    assert True


@pytest.mark.usefixtures("fruits")
class BaseTest:
    pass


class TestFruits(BaseTest):

    def test_small_fruit(self):
        print(f"Small fruit is: {self.fruits}")
        assert True

    # @pytest.mark.depends(on=["TestFruits::test_large_fruit"])
    def test_medium_fruit(self):
        print(f"Medium fruit is: {self.fruits}")
        assert True

    def test_large_fruit(self):
        print(f"Large fruit is: {self.fruits}")
        assert True
