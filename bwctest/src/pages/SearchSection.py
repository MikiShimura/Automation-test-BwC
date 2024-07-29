from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.SearchSectionLocators import SearchSectionLocators

class SearchSection(SearchSectionLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def choose_categories_on_seach_section(self, categories=2):
        checkboxes = [self.CATEGORY_CHECKBOX_CULTURE, self.CATEGORY_CHECKBOX_SPORT, 
                      self.CATEGORY_CHECKBOX_ENTERTAINMENT, self.CATEGORY_CHECKBOX_NATURE,
                      self.CATEGORY_CHECKBOX_EDUCATION]
        
        if categories > 5:
            print("Argument of function 'choose_categories_on_seach_section' should be lower than 6")
        for n in range(categories): 
            self.sl.wait_and_click(checkboxes[n])
        
        # I want to choose category random but code below doesn't work. Consider later.
        # if categories > 5:
        #     print("Argument of function 'choose_ages_on_seach_section' should be lower than 6")
        # else:
        #     rand_categories = random.sample(checkboxes, categories)
        #     print(rand_categories)
        #     for i in rand_categories: 
        #         print(i)
        #         self.sl.wait_and_click(i[0], i[1])

    def choose_ages_on_seach_section(self, ages=2):
        checkboxes = [self.AGES_CHECKBOX_0_1, self.AGES_CHECKBOX_2_3, self.AGES_CHECKBOX_4_6, 
                      self.AGES_CHECKBOX_7_9, self.AGES_CHECKBOX_10]
        if ages > 5:
            print("Argument of function 'choose_ages_on_seach_section' should be lower than 6")
        for n in range(ages): 
            self.sl.wait_and_click(checkboxes[n])

    def click_search_button(self):
        self.sl.wait_and_click(self.SEARCH_BTN)

        