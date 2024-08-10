from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.AlertLocators import AlertLocators

class Alert(AlertLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def wait_until_success_message_is_displayed(self, exp_msg):
        self.sl.wait_until_element_contains_text(self.ALERT_SUCCESS_MSG, exp_msg)

    def wait_until_error_message_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ALERT_ERR_MSG, exp_err)