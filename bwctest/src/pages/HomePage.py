from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.HomePageLocators import HomePageLocators
from src.helpers.config_helpers import get_base_url
from selenium.webdriver.common.by import By
import random
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, TimeoutException
import time

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    
    def go_to_homepage(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    # def get_success_message(self):
    #     return self.sl.wait_and_get_text(self.ALERT_SUCCESS_MESSAGE)
    
    def wait_until_app_image_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.APP_IMG)

    def get_app_image_element(self):
        element = self.sl.wait_and_get_element(self.APP_IMG)
        return element
    
    def wait_until_map_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.MAIN_MAP)

    def get_map_element(self):
        element = self.sl.wait_and_get_element(self.MAIN_MAP)
        return element

    def wait_until_sites_section_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITES_SEC)

    def get_sites_section_element(self):
        element = self.sl.wait_and_get_element(self.SITES_SEC)
        return element
    
    def get_all_sites(self):
        try:
            return self.sl.wait_and_get_elements(self.ALL_SITE_CARDS)
        except TimeoutException:
            return 0
    
    def get_site_title(self, parent):
        return parent.find_element(self.SITE_TITLE[0], self.SITE_TITLE[1]).text
    
    def wait_until_site_image_is_displayed(self, parent):
        elm = parent.find_element(self.SITE_IMG[0], self.SITE_IMG[1])
        elm.is_displayed()
        
    def wait_until_site_title_is_displayed(self, parent):
        elm = parent.find_element(self.SITE_TITLE[0], self.SITE_TITLE[1])
        elm.is_displayed()
    
    def wait_until_site_category_is_displayed(self, parent):
        elm = parent.find_element(self.SITE_CATEGORIES[0], self.SITE_CATEGORIES[1])
        elm.is_displayed()
    
    def wait_until_site_ages_are_displayed(self, parent):
        elm = parent.find_element(self.SITE_AGES[0], self.SITE_AGES[1])
        elm.is_displayed()

    def wait_until_search_result_text_is_displayed(self):
        return self.sl.wait_and_get_text(self.SEARCH_RESULT_MSG)
    
    def click_site(self, number):
        try:
            self.driver.find_element(By.XPATH, f'/html/body/main/div[2]/div/div[3]/div[2]/div[{number}]/a/div').click()
        except ElementNotInteractableException:
            time.sleep(2)
            self.driver.find_element(By.XPATH, f'/html/body/main/div[2]/div/div[3]/div[2]/div[{number}]/a/div').click()
        except NoSuchElementException:
            time.sleep(2)
            self.driver.find_element(By.XPATH, f'/html/body/main/div[2]/div/div[3]/div[2]/div[{number}]/a/div').click()

    def click_random_site(self):
        number = len(self.get_all_sites())
        random_number = random.randint(1, number)

        self.click_site(random_number)

        return random_number