from selenium.webdriver.common.by import By

class HomePageLocators():
    ALERT_SUCCESS_MSG = (By.XPATH, "/html/body/main/div[1]")

    NAVIGATION_SEC = (By.CSS_SELECTOR, "nav")
    APP_IMG = (By.XPATH, "/html/body/main/div[1]")
    MAP_SEC = (By.CSS_SELECTOR, "canvas")
    SEARCH_SEC = (By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div")
    INDEX_MAP_SEC = (By.ID, "index-map")
    SITES_SEC = (By.XPATH, "/html/body/main/div[2]/div/div[3]/div[2]")

    ALL_SITE_CARDS = (By.CSS_SELECTOR, "div.card")
    SITE_IMG = (By.CSS_SELECTOR, "img.card-img-top")
    SITE_TITLE = (By.CSS_SELECTOR, "h5.card-title")
    SITE_CATEGORIES = (By.CSS_SELECTOR, "p.card-text span.badge.rounded-pill")
    SITE_AGES = (By.CSS_SELECTOR, "p.card-text span.badge.bg-secondary")

    SEARCH_RESULT_MSG = (By.XPATH, "/html/body/main/div[2]/div/div[3]/div[2]/p")