from selenium.webdriver.common.by import By

class SiteDetailedPageLocators():
    SITE_TITLE = (By.CSS_SELECTOR, 'h2')
    SITE_IMAGES = (By.CSS_SELECTOR, 'div.carousel-item img')
    SITE_ADDRESS = (By.XPATH, '/html/body/main/div[1]/div[1]/p[1]')
    SITE_DESCRIPTION = (By.XPATH, '/html/body/main/div[1]/div[1]/p[2]')
    SITE_CATEGORY = (By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/p[1]')
    SITE_AGES = (By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/p[2]')
    SITE_PRICE = (By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/p[3]')
    SITE_URL = (By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/p[4]')
    SITE_MAP = (By.ID, 'map')

    SITE_REVIEWS = (By.CSS_SELECTOR, 'div.card-body')
    REVIEW_LABEL = (By.CSS_SELECTOR, 'h3')

    OPEN_REVIEW_FORM_BTN = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/button')
    RATING_STAR_1 = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/div/div/div[2]/form/div[1]/fieldset/label[1]')
    RATING_STAR_2 = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/div/div/div[2]/form/div[1]/fieldset/label[2]')
    RATING_STAR_3 = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/div/div/div[2]/form/div[1]/fieldset/label[3]')
    RATING_STAR_4 = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/div/div/div[2]/form/div[1]/fieldset/label[4]')
    RATING_STAR_5 = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/div/div/div[2]/form/div[1]/fieldset/label[5]')
    COMMENT_FIELD = (By.CSS_SELECTOR, 'textarea')
    POST_REVIEW_BTN = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/div/div/div[2]/form/div[3]/button')
    REVIEW_FORM_LABEL = (By.ID, 'reviewModalLabel')

    STAR_ON_REVIEW = (By.CSS_SELECTOR, 'div.card-body p.starability-result')
    COMMENT_ON_REVIEW = (By.XPATH, '/html/body/main/div[4]/div[1]/div/p[2]')
    USERNAME_ON_REVIEW = (By.XPATH, '/html/body/main/div[4]/div[1]/div/p[3]')
    DELETE_REVIEW_BTN = (By.XPATH, '/html/body/main/div[3]/div[{n}]/div/form/button')

    INVARID_ALERT_COMMENT = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/div/div/div[2]/form/div[2]/div')
