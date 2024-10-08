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

    def click_post_new_site_button(self):
        self.sl.wait_and_click(self.POST_BTN)

    def wait_until_nav_bar_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.NAV_BAR)

    def get_nav_element(self):
        element = self.sl.wait_and_get_element(self.NAV_BAR)
        return element
    
    def wait_until_logout_button_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.LOGOUT_BTN)
    
    def click_logout_button(self):
        self.sl.wait_and_click(self.LOGOUT_BTN)

    def wait_until_login_button_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.LOGIN_BTN)

    def wait_until_register_button_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.REGISTER_BTN)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BTN)

    def click_register_button(self):
        self.sl.wait_and_click(self.REGISTER_BTN)

    def click_site_logo(self):
        self.sl.wait_and_click(self.SITE_LOGO)