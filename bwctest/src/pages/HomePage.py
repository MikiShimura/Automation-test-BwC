from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.HomePageLocators import HomePageLocators
from src.helpers.config_helpers import get_base_url

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    
    def go_to_homepage(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    # def get_success_message(self):
    #     return self.sl.wait_and_get_text(self.ALERT_SUCCESS_MESSAGE)
    
    def wait_until_success_message_is_displayed(self, exp_msg):
        self.sl.wait_until_element_contains_text(self.ALERT_SUCCESS_MSG, exp_msg)

    def wait_until_navigation_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.NAVIGATION_SEC)

    def get_navigation_element(self):
        elements = self.sl.wait_and_get_elements(self.NAVIGATION_SEC)
        return elements[0]