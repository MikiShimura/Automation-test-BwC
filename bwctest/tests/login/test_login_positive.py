import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.configs.generic_configs import GenericConfigs
from src.helpers.config_helpers import get_base_url


@pytest.mark.usefixtures("init_driver")
class TestLoginPositive:

    @pytest.mark.tcid103
    def test_login_existing_admin(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)

        login.go_to_login()
        login.input_login_username(GenericConfigs.ADMIN_NAME)
        login.input_login_password(GenericConfigs.ADMIN_PASS)
        login.click_login_button()

        # check expected_text
        expected_message = GenericConfigs.LOGIN_SUCCESS_MSG 
        homepage.wait_until_success_message_is_displayed(expected_message)

        # success_message = homepage.get_success_message()
        # expected_message = "Welcome back!"
        # assert success_message==expected_message, "Login success message is not displayed correctly."

        # check url
        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page or Login failed."


    @pytest.mark.tcid106
    def test_login_existing_user(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)

        login.go_to_login()
        login.input_login_username(GenericConfigs.VALID_USER_NAME)
        login.input_login_password(GenericConfigs.VALID_USER_PASS)
        login.click_login_button()

        # check expected_text
        expected_message = GenericConfigs.LOGIN_SUCCESS_MSG 
        homepage.wait_until_success_message_is_displayed(expected_message)
        
        # check url
        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page or Login failed."

        