from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.RegisterPageLocators import RegisterPageLocators
from src.helpers.config_helpers import get_base_url

class RegisterPage(RegisterPageLocators):

    endpoint = "user/register"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_register(self):
        base_url = get_base_url()
        login_url = base_url + self.endpoint
        self.driver.get(login_url)

    def input_register_username(self, username):
        self.sl.wait_and_input_text(self.REGISTER_USERNAME, username)
    
    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)
    
    def click_register_button(self):
        self.sl.wait_and_click(self.REGISTER_BTN)

    def wait_until_username_label_is_displayed(self, exp_text):
        self.sl.wait_until_element_contains_text(self.REGISTER_USERNAME_LABEL, exp_text)
    
    def wait_until_email_label_is_displayed(self, exp_text):
        self.sl.wait_until_element_contains_text(self.REGISTER_EMAIL_LABEL, exp_text)

    def wait_until_password_label_is_displayed(self, exp_text):
        self.sl.wait_until_element_contains_text(self.REGISTER_PASSWORD_LABEL, exp_text)

    def wait_until_register_button_is_displayed(self, exp_text):
        self.sl.wait_until_element_contains_text(self.REGISTER_BTN, exp_text)