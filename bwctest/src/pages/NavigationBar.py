from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.NavigationBarLocators import NavigationBarLocators

class NavigationBar(NavigationBarLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def wait_until_post_button_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.POST_BTN)

    def wait_until_post_button_is_not_displayed(self):
        self.sl.wait_until_element_is_invisible(self.POST_BTN)