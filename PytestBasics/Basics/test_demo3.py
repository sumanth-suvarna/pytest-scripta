import pytest


@pytest.fixture
def setup():
    dash = 'dashboard'
    print("RUNNING FIXTURE BEFORE TEST CASE")
    yield dash
    print("RUNNING FIXTURE AFTER TEST CASE")


# @pytest.mark.depends(on='test_discovery_status')
def test_devices(setup):
    print(setup)
    assert "devices" == "device", "FAIL: Devices not discovered"


@pytest.mark.sanity
def test_discovery_status(setup):
    print(setup)
    print("Discovery Completed")
    assert "discover" == "discovery", "FAIL: Discovery Failed"


def test_all_is_well():
    print("All is Well")
    assert True


def test_better_is_well():
    print("Better is Well")
    assert True

