from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_USERNAME = (By.ID, "username")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "/html/body/main/div/div/div/div/div/form/div[3]/button")

    ALERT_ERR_MSG = (By.XPATH, "/html/body/main/div[1]")