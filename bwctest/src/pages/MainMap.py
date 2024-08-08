from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.MainMapLocators import MainMapLocators

class MainMap(MainMapLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def wait_until_pins_are_displayed(self):
        self.sl.wait_until_element_is_visible(self.PINS_ON_MAP)

    def click_pin(self):
        self.sl.wait_and_click(self.PINS_ON_MAP)
    
    def wait_until_popup_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.POPUP_ON_MAP)
    
    def wait_until_popup_is_not_displayed(self):
        self.sl.wait_until_element_is_invisible(self.POPUP_ON_MAP)
    
    def get_link_text_on_popup(self):
        return self.sl.wait_and_get_text(self.LINK_ON_POPUP)

    def click_link_on_popup(self):
        self.sl.wait_and_click(self.LINK_ON_POPUP)

    def click_close_button_on_popup(self):
        self.sl.wait_and_click(self.CLOSE_BTN_ON_POPUP)

    def click_zoom_out(self):
        self.sl.wait_and_click(self.ZOOM_OUT_BTN)

    def get_pins(self):
        return self.sl.wait_and_get_elements(self.PINS_ON_MAP)