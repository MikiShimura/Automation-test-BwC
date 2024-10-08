from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.SearchSectionLocators import SearchSectionLocators
import random
from selenium.common.exceptions import ElementNotInteractableException
import time

class SearchSection(SearchSectionLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def choose_categories_on_seach_section(self, categories=2):
        checkboxes = [self.CATEGORY_CHECKBOX_CULTURE, self.CATEGORY_CHECKBOX_SPORT, 
                      self.CATEGORY_CHECKBOX_ENTERTAINMENT, self.CATEGORY_CHECKBOX_NATURE,
                      self.CATEGORY_CHECKBOX_EDUCATION]
        
        if categories < 0 or categories > 5:
            print("Argument of function 'choose_ages_on_seach_section' should be from 1 to 5")

        else:
            rand_categories = random.sample(checkboxes, categories)
            try:
                for i in rand_categories: 
                    self.driver.find_element(i[0], i[1]).click()
            except ElementNotInteractableException:
                self.driver.execute_script("window.scrollTo(0, 500)")
                time.sleep(2)
                for i in rand_categories: 
                    self.driver.find_element(i[0], i[1]).click()

    def choose_ages_on_seach_section(self, ages=2):
        checkboxes = [self.AGES_CHECKBOX_0_1, self.AGES_CHECKBOX_2_3, self.AGES_CHECKBOX_4_6, 
                      self.AGES_CHECKBOX_7_9, self.AGES_CHECKBOX_10]
        if ages < 0 or ages > 5:
            print("Argument of function 'choose_ages_on_seach_section' should be from 1 to 5")

        else:
            rand_ages = random.sample(checkboxes, ages)
            try:
                for i in rand_ages: 
                    self.driver.find_element(i[0], i[1]).click()
            except ElementNotInteractableException:
                self.driver.execute_script("window.scrollTo(0, 500)")
                time.sleep(2)
                for i in rand_ages: 
                    self.driver.find_element(i[0], i[1]).click()

    def click_search_button(self):
        try:
            self.sl.wait_and_click(self.SEARCH_BTN)
        except ElementNotInteractableException:
            self.driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            self.sl.wait_and_click(self.SEARCH_BTN)

    def click_clear_all_button(self):
        try:
            self.sl.wait_and_click(self.CLEAR_ALL_BTN)
        except ElementNotInteractableException:
            self.driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            self.sl.wait_and_click(self.CLEAR_ALL_BTN)
    
    def wait_until_category_labels_are_displayed(self, exp_text_1, exp_text_2, exp_text_3, exp_text_4, exp_text_5):
        self.sl.wait_until_element_contains_text(self.CATEGORY_LABEL_CULTURE, exp_text_1)
        self.sl.wait_until_element_contains_text(self.CATEGORY_LABEL_SPORT, exp_text_2)
        self.sl.wait_until_element_contains_text(self.CATEGORY_LABEL_ENTERTAINMENT, exp_text_3)
        self.sl.wait_until_element_contains_text(self.CATEGORY_LABEL_NATURE, exp_text_4)
        self.sl.wait_until_element_contains_text(self.CATEGORY_LABEL_EDUCATION, exp_text_5)
    
    def wait_until_age_labels_are_displayed(self, exp_text_1, exp_text_2, exp_text_3, exp_text_4, exp_text_5):
        self.sl.wait_until_element_contains_text(self.AGES_LABEL_0_1, exp_text_1)
        self.sl.wait_until_element_contains_text(self.AGES_LABEL_2_3, exp_text_2)
        self.sl.wait_until_element_contains_text(self.AGES_LABEL_4_6, exp_text_3)
        self.sl.wait_until_element_contains_text(self.AGES_LABEL_7_9, exp_text_4)
        self.sl.wait_until_element_contains_text(self.AGES_LABEL_10, exp_text_5)

    def wait_until_search_button_displayed(self, exp_text):
        self.sl.wait_until_element_contains_text(self.SEARCH_BTN, exp_text)

    def wait_until_clear_all_button_displayed(self, exp_text):
        self.sl.wait_until_element_contains_text(self.CLEAR_ALL_BTN, exp_text)
        
    def categories_are_not_selected(self):
        if not (self.driver.find_element(self.CATEGORY_CHECKBOX_CULTURE[0], self.CATEGORY_CHECKBOX_CULTURE[1]).is_selected()
                or self.driver.find_element(self.CATEGORY_CHECKBOX_SPORT[0], self.CATEGORY_CHECKBOX_SPORT[1]).is_selected()
                or self.driver.find_element(self.CATEGORY_CHECKBOX_ENTERTAINMENT[0], self.CATEGORY_CHECKBOX_ENTERTAINMENT[1]).is_selected()
                or self.driver.find_element(self.CATEGORY_CHECKBOX_NATURE[0], self.CATEGORY_CHECKBOX_NATURE[1]).is_selected()
                or self.driver.find_element(self.CATEGORY_CHECKBOX_EDUCATION[0], self.CATEGORY_CHECKBOX_EDUCATION[1]).is_selected()):
            return True
        
#   TimeOutError occur if func self.sl.wait_until_element_is_selected() is used
        
    def ages_are_not_selected(self):
        if not (self.driver.find_element(self.AGES_CHECKBOX_0_1[0], self.AGES_CHECKBOX_0_1[1]).is_selected()
                or self.driver.find_element(self.AGES_CHECKBOX_2_3[0], self.AGES_CHECKBOX_2_3[1]).is_selected()
                or self.driver.find_element(self.AGES_CHECKBOX_4_6[0], self.AGES_CHECKBOX_4_6[1]).is_selected()
                or self.driver.find_element(self.AGES_CHECKBOX_7_9[0], self.AGES_CHECKBOX_7_9[1]).is_selected()
                or self.driver.find_element(self.AGES_CHECKBOX_10[0], self.AGES_CHECKBOX_10[1]).is_selected()):
            return True
        


        