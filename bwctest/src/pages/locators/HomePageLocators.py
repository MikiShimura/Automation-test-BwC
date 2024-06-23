from selenium.webdriver.common.by import By

class HomePageLocators():
    ALERT_SUCCESS_MSG = (By.XPATH, "/html/body/main/div[1]")

    NAVIGATION_SEC = (By.CSS_SELECTOR, "nav")
    APP_IMG = (By.XPATH, "/html/body/main/div[1]")
    SEARCH_SEC = (By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div")
    INDEX_MAP_SEC = (By.ID, "index-map")
    SITES_SEC = (By.XPATH, "/html/body/main/div[2]/div/div[3]/div[2]")