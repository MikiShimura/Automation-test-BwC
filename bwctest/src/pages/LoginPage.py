from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.LoginPageLocators import LoginPageLocators
from src.helpers.config_helpers import get_base_url

class LoginPage(LoginPageLocators):

    endpoint = "/user/login"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_login(self):
        base_url = get_base_url()
        login_url = base_url + self.endpoint
        self.driver.get(login_url)
