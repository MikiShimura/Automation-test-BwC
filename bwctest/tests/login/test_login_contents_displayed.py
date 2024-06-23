import pytest
from src.pages.LoginPage import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestContentDisplayed:

    @pytest.mark.tcid101
    def test_correct_username_and_password_labels_are_displayed(self):
        login = LoginPage(self.driver)

        login.go_to_login()
        login.wait_until_username_label_is_displayed("Username")
        login.wait_until_password_label_is_displayed("Password")

    @pytest.mark.tcid102
    def test_correct_login_button_is_displayed(self):
        login = LoginPage(self.driver)

        login.go_to_login()
        login.wait_until_login_button_is_displayed("Login")

