import pytest


# @pytest.mark.depends(on='test_discovery_status')
def test_devices():
    assert "devices" == "devices", "FAIL: Devices not discovered"


@pytest.mark.sanity
def test_discovery_status():
    print("Discovery Completed")
    assert "discovery" == "discovery", "FAIL: Discovery Failed"


def test_all_is_well():
    print("All is Well")
    assert True


def test_better_is_well():
    assert True

