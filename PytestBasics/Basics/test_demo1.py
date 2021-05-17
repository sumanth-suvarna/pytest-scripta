import pytest


def setup_module(module):
    print("RUNNING SETUP")


def teardown_module(module):
    print("RUNNING TEARDOWN")


@pytest.mark.sanity
def test_username():
    assert "sumanth" == "sumanth", "FAIL: Username is invalid"
    print("End Of Test")


@pytest.mark.smoke
@pytest.mark.sanity
def test_login():
    assert "s" in "login", "FAIL: Login Failed"
    print("End Of Test")


def test_auth():
    assert "auth" == "auth", "FAIL: Login Failed"
    print("End Of Test")