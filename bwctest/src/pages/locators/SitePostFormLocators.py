from selenium.webdriver.common.by import By

class SitePostFormLocators():
    TITLE_FIELD = (By.ID, "title")
    DESCRIPTION_FIELD = (By.ID, "description")
    CATEGORY_RADIO_CULTURE = (By.CSS_SELECTOR, 'input[value="Culture"]')
    CATEGORY_RADIO_SPORT = (By.CSS_SELECTOR, 'input[value="Sport"]')
    CATEGORY_RADIO_ENTERTAINMENT = (By.CSS_SELECTOR, 'input[value="Entertainment"]')
    CATEGORY_RADIO_NATURE = (By.CSS_SELECTOR, 'input[value="Nature"]')
    CATEGORY_RADIO_EDUCATION = (By.CSS_SELECTOR, 'input[value="Education"]')
    AGES_CHECKBOX_0_1 = (By.CSS_SELECTOR, 'input[value="0~1"]')
    AGES_CHECKBOX_2_3 = (By.CSS_SELECTOR, 'input[value="2~3"]')
    AGES_CHECKBOX_4_6 = (By.CSS_SELECTOR, 'input[value="4~6"]')
    AGES_CHECKBOX_7_9 = (By.CSS_SELECTOR, 'input[value="7~9"]')
    AGES_CHECKBOX_10 = (By.CSS_SELECTOR, 'input[value="10~"]')
    LOCATION_FIELD = (By.ID, "location")
    LONGTITUDE_FIELD = (By.ID, "longtitude")
    LATITUDE_FIELD = (By.ID, "latitude")
    URL_FIELD = (By.ID, "url")
    PRICE_FIELD = (By.ID, "price")
    IMG_UPROAD_BTN = (By.ID, "image")

    DONE_BTN = (By.XPATH, "/html/body/main/div/div/form/div[11]/button")
    EDIT_BTN = (By.XPATH, "/html/body/main/div/div/form/div[12]/button")

    INVALID_ALERT = (By.CSS_SELECTOR, "div.invalid-feedback")
    INVALID_ALERT_TITLE = (By.XPATH, "/html/body/main/div/div/form/div[1]/div")
    INVALID_ALERT_DESCRIPTION = (By.XPATH, "/html/body/main/div/div/form/div[2]/div")
    INVALID_ALERT_LOCATION = (By.XPATH, "/html/body/main/div/div/form/div[5]/div")
    INVALID_ALERT_LONGTITUDE = (By.XPATH, "/html/body/main/div/div/form/div[6]/div")
    INVALID_ALERT_LATITUDE = (By.XPATH, "/html/body/main/div/div/form/div[7]/div")
    INVALID_ALERT_PRICE = (By.XPATH, "/html/body/main/div/div/form/div[9]/div")