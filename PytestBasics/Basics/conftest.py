import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


@pytest.fixture(scope='session')
def started_tests():
    print("STARTED TEST EXECUTION")
    yield
    print("ENDING TEST EXECUTION")


@pytest.fixture(scope='session', autouse=True)
def start_tests():
    print("STARTING TEST EXECUTION")
    yield
    print("ENDED TEST EXECUTION")


@pytest.fixture(params=["chrome", "edge"], scope='class')
def initialize_driver(request):
    print("INITIALIZING DRIVER")
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == "edge":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    # web_driver.get("http://www.google.com")

    yield request.cls.driver
    print("CLOSING DRIVER")
    web_driver.close()


@pytest.fixture(params=["chrome"], scope='module')
def get_driver(request):
    print(f"INITIALIZING DRIVER - {request.param}")
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == "edge":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    web_driver.implicitly_wait(5)
    web_driver.maximize_window()
    # web_driver.get("http://www.google.com")

    yield web_driver
    print(f"CLOSING DRIVER - {request.param}")
    web_driver.close()


@pytest.fixture(scope='module')
def req_module_context(request):
    url = getattr(request.module, "url", "www.python.org")
    return url
