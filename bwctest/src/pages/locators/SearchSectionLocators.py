from selenium.webdriver.common.by import By

class SearchSectionLocators():
    # There are 2search section(for mobile and for laptop, only 1 is always displayed), be careful for the locators
    CATEGORY_CHECKBOX_CULTURE = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/input[1]')
    CATEGORY_CHECKBOX_SPORT = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/input[2]')
    CATEGORY_CHECKBOX_ENTERTAINMENT = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/input[3]')
    CATEGORY_CHECKBOX_NATURE = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/input[4]')
    CATEGORY_CHECKBOX_EDUCATION = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/input[5]')
    AGES_CHECKBOX_0_1 = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/input[6]')
    AGES_CHECKBOX_2_3 = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/input[7]')
    AGES_CHECKBOX_4_6 = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/input[8]')
    AGES_CHECKBOX_7_9 = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/input[9]')
    AGES_CHECKBOX_10 = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/input[10]')
    SEARCH_BTN = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[1]/button')
    CLEAR_ALL_BTN = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/form[2]/button')