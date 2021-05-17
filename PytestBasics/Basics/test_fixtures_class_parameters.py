import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["chrome", "edge"], scope="class")
def init_driver(request):
    print(f"INITIALIZING DRIVER - {request.param}")
    web_driver = None
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == "edge":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    request.cls.driver = web_driver
    web_driver.get("http://www.google.com")
    yield web_driver
    print(f"CLOSING DRIVER - {request.param}")
    web_driver.close()


@pytest.mark.usefixtures("init_driver")
class DriverBaseTest:
    pass


class TestGoogle(DriverBaseTest):

    def test_search(self):
        print("Searching Selenium")
        self.driver.find_element_by_name("q").send_keys("selenium")
        self.driver.find_element(By.CSS_SELECTOR, "div.FPdoLc.tfB0Bf input[value='Google Search']").click()
        time.sleep(2)
        assert True

    @pytest.mark.depends(on=['TestGoogle::test_title'])
    def test_get_url(self):
        print("Testing URL")
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl", "FAIL: Current URL expected is " \
                                                                                "https://www.google1.com/?gws_rd=ssl "\
                                                                                f"but received {self.driver.current_url}"

    def test_title(self):
        print("Testing Title")
        assert self.driver.title == "Google", f"FAIL: Title expected is Google but received {self.driver.title}"
