import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = chrome_driver
    chrome_driver.get("http://www.google.com")
    yield
    chrome_driver.close()


@pytest.fixture(scope='class')
def init_edge_driver(request):
    edge_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    request.cls.driver = edge_driver
    edge_driver.get("http://www.google.com")
    yield
    edge_driver.close()


@pytest.mark.usefixtures("init_chrome_driver")
class BaseChromeTest:
    pass


@pytest.mark.usefixtures("init_edge_driver")
class BaseEdgeTest:
    pass


class TestGoogleChrome(BaseChromeTest):

    def test_title(self):
        assert self.driver.title == "Google"

    def test_get_url(self):
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"


class TestGoogleEdge(BaseEdgeTest):

    def test_title(self):
        assert self.driver.title == "Google"

    def test_get_url(self):
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"
