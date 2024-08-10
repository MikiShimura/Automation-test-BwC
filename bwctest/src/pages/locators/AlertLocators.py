from selenium.webdriver.common.by import By

class AlertLocators():
    ALERT_SUCCESS_MSG = (By.XPATH, "/html/body/main/div[1]")
    ALERT_ERR_MSG = (By.XPATH, "/html/body/main/div[1]")
