import pytest


@pytest.fixture(scope='module')
def setup():
    dash = 'dashboard'
    print("RUNNING FIXTURE BEFORE TEST CASE")
    yield dash
    print("RUNNING FIXTURE AFTER TEST CASE")


@pytest.mark.sanity
# @pytest.mark.smoke
def test_post_login(setup):
    print(setup)
    assert setup == "dashboard", "FAIL: Failed to display dashboard"


@pytest.mark.smoke
@pytest.mark.usefixtures("setup")
def test_discovery():
    assert "disc" in "discovery", "FAIL: Discovery Failed"