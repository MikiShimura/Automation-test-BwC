import pytest
from src.pages.LoginPage import LoginPage

@pytest.mark.usefixtures("init_driver")
class TestLoginPositive:

    @pytest.mark.tcid103
    def test_login_existing_admin(self):
        login = LoginPage(self.driver)
        login.go_to_login()
        # my_account.go_to_my_account()
        # my_account.input_login_username("asdfghjk")
        # my_account.input_login_password("asdf1234")
        # my_account.click_login_button()

        # expected_err = "Error: The username asdfghjk is not registered on this site. If you are unsure of your username, try your email address instead."
        # my_account.wait_until_error_is_displayed(expected_err)