from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.HomePageLocators import HomePageLocators
from src.helpers.config_helpers import get_base_url
from selenium.webdriver.common.by import By

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
    
    def wait_until_app_image_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.APP_IMG)

    def get_app_image_element(self):
        elements = self.sl.wait_and_get_elements(self.APP_IMG)
        return elements[0]
    
    def wait_until_map_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.MAP_SEC)

    def get_map_element(self):
        elements = self.sl.wait_and_get_elements(self.MAP_SEC)
        return elements[0]

    def wait_until_sites_section_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITES_SEC)

    def get_sites_section_element(self):
        elements = self.sl.wait_and_get_elements(self.SITES_SEC)
        return elements[0]
    
    def get_all_sites(self):
        return self.sl.wait_and_get_elements(self.ALL_SITE_CARDS)

    def get_site_image(self, parent):
        return parent.find_element(By.CSS_SELECTOR, 'img.a')
    
    def get_site_title(self, parent):
        return parent.find_element(self.SITE_TITLE[0], self.SITE_TITLE[1])
    
    def get_site_categories(self, parent):
        return parent.find_element(self.SITE_CATEGORIES[0], self.SITE_CATEGORIES[1])
    
    def get_site_ages(self, parent):
        return parent.find_element(self.SITE_AGES[0], self.SITE_AGES[1])