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

    def wait_until_address_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_ADDRESS)

    def wait_until_description_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_DESCRIPTION)

    def wait_until_category_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_CATEGORY)

    def wait_until_ages_are_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_AGES)
    
    def wait_until_price_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_PRICE)

    def wait_until_url_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_URL)

    def wait_until_map_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_MAP)