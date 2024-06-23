import pytest
from src.pages.RegisterPage import RegisterPage


@pytest.mark.usefixtures("init_driver")
class TestContentDisplayed:

    @pytest.mark.tcid201
    def test_correct_username_and_password_labels_are_displayed(self):
        register = RegisterPage(self.driver)

        register.go_to_register()
        register.wait_until_username_label_is_displayed("Username")
        register.wait_until_email_label_is_displayed("Mail address")
        register.wait_until_password_label_is_displayed("Password")

    @pytest.mark.tcid202
    def test_correct_login_button_is_displayed(self):
        register = RegisterPage(self.driver)

        register.go_to_register()
        register.wait_until_register_button_is_displayed("Register")

