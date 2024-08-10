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

    POST_REVIEW_BTN = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/button')

    STAR_ON_REVIEW = (By.CSS_SELECTOR, 'div.card-body p.starability-result')
    COMMENT_ON_REVIEW = (By.XPATH, '/html/body/main/div[4]/div[1]/div/p[2]')
    USERNAME_ON_REVIEW = (By.XPATH, '/html/body/main/div[4]/div[1]/div/p[3]')