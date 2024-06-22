from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.HomePageLocators import HomePageLocators

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # def get_success_message(self):
    #     return self.sl.wait_and_get_text(self.ALERT_SUCCESS_MESSAGE)
    
    def wait_until_success_message_is_displayed(self, exp_msg):
        self.sl.wait_until_element_contains_text(self.ALERT_SUCCESS_MSG, exp_msg)