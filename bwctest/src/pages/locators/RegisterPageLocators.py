from selenium.webdriver.common.by import By

class RegisterPageLocators():
    REGISTER_USERNAME_LABEL = (By.XPATH, "/html/body/main/div/div/div/div/div/form/div[1]/label")
    REGISTER_USERNAME = (By.ID, "username")
    REGISTER_EMAIL_LABEL = (By.XPATH, "/html/body/main/div/div/div/div/div/form/div[2]/label")
    REGISTER_EMAIL = (By.ID, "email")
    REGISTER_PASSWORD_LABEL = (By.XPATH, "/html/body/main/div/div/div/div/div/form/div[3]/label")
    REGISTER_PASSWORD = (By.ID, "password")
    REGISTER_BTN = (By.XPATH, "/html/body/main/div/div/div/div/div/form/div[4]/button")
