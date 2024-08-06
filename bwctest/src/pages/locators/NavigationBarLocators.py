from selenium.webdriver.common.by import By

class NavigationBarLocators():
    SITE_LOGO = (By.XPATH, '/html/body/nav/div/a')
    POST_BTN = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/a')
    LOGIN_BTN = (By.XPATH, '/html/body/nav/div/div/div[2]/a[1]')
    LOGOUT_BTN = (By.XPATH, '/html/body/nav/div/div/div[2]/a')
    REGISTER_BTN = (By.XPATH, '/html/body/nav/div/div/div[2]/a[2]')
    NAV_BAR = (By.CSS_SELECTOR, "nav")

    