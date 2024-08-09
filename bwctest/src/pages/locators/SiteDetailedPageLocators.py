from selenium.webdriver.common.by import By

class SiteDetailedPageLocators():
    SITE_TITLE = (By.CSS_SELECTOR, 'h2')
    SITE_IMAGES = (By.CSS_SELECTOR, 'div.carousel-item img')