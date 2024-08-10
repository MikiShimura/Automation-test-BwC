from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_USERNAME_LABEL = (By.XPATH, "/html/body/main/div/div/div/div/div/form/div[1]/label")
    LOGIN_USERNAME = (By.ID, "username")
    LOGIN_PASSWORD_LABEL = (By.XPATH, "/html/body/main/div/div/div/div/div/form/div[2]/label")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "/html/body/main/div/div/div/div/div/form/div[3]/button")