from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.SearchSectionLocators import SearchSectionLocators
import random

class SearchSection(SearchSectionLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def choose_categories_on_seach_section(self, categories=2):
        checkboxes = [self.CATEGORY_CHECKBOX_CULTURE, self.CATEGORY_CHECKBOX_SPORT, 
                      self.CATEGORY_CHECKBOX_ENTERTAINMENT, self.CATEGORY_CHECKBOX_NATURE,
                      self.CATEGORY_CHECKBOX_EDUCATION]
        
        if categories > 5:
            print("Argument of function 'choose_ages_on_seach_section' should be lower than 6")
        else:
            rand_categories = random.sample(checkboxes, categories)
            for i in rand_categories: 
                self.driver.find_element(i[0], i[1]).click()

    def choose_ages_on_seach_section(self, ages=2):
        checkboxes = [self.AGES_CHECKBOX_0_1, self.AGES_CHECKBOX_2_3, self.AGES_CHECKBOX_4_6, 
                      self.AGES_CHECKBOX_7_9, self.AGES_CHECKBOX_10]
        if ages > 5:
            print("Argument of function 'choose_ages_on_seach_section' should be lower than 6")
        else:
            rand_ages = random.sample(checkboxes, ages)
            for i in rand_ages: 
                self.driver.find_element(i[0], i[1]).click()

    def click_search_button(self):
        self.sl.wait_and_click(self.SEARCH_BTN)

        