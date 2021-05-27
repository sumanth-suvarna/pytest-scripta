import time

import pytest


# @pytest.mark.order(1)
def test_google(get_driver):
    web_driver = get_driver
    web_driver.get("https://www.google.com")
    time.sleep(2)
    assert True


@pytest.mark.parametrize(
                            "search",
                            [
                                "Selenium",
                                "Python"
                            ]
                        )
# @pytest.mark.order(2)
def test_search(get_driver, search):
    web_driver = get_driver
    web_driver.find_element_by_name("q").send_keys(search)
    time.sleep(2)
    print(search)
    web_driver.find_element_by_name("q").clear()
    time.sleep(2)
    assert True
