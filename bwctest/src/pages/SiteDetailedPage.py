from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.SiteDetailedPageLocators import SiteDetailedPageLocators

class SiteDetailedPage(SiteDetailedPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def get_site_title_text(self):
        return self.sl.wait_and_get_text(self.SITE_TITLE)
    
    def wait_until_title_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_TITLE)

    def wait_until_image_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_IMAGES)

    