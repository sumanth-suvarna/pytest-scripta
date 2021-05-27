import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
    pass


class TestHubSport(BaseTest):

    @pytest.mark.parametrize(
                                "username, password",
                                [
                                    ("sumanth.suvarna1@gmail.com", "passwd1"),
                                    ("sumanth.suvarna2@gmail.com", "passwd2")
                                ]
                             )
    def test_login(self, username, password):
        self.driver.get("https://app.hubspot.com")
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)


class TestHubSport2(BaseTest):

    @pytest.mark.parametrize(
                                "username, password",
                                [
                                    ("sumanth.suvarna1@gmail.com", "passwd1"),
                                    ("sumanth.suvarna2@gmail.com", "passwd2")
                                ]
                             )
    def test_login(self, username, password):
        self.driver.get("https://app.hubspot.com")
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)

