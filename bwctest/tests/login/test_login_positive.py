import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.configs.generic_configs import GenericConfigs
from src.helpers.config_helpers import get_base_url


@pytest.mark.usefixtures("init_driver")
class TestLoginPositive:

    @pytest.mark.tcid103
    def test_login_existing_admin(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        login.valid_login(admin=True)

        # check expected_text
        expected_message = GenericConfigs.LOGIN_SUCCESS_MSG 
        homepage.wait_until_success_message_is_displayed(expected_message)

        # check if logout bottun is displayed
        navigation.wait_until_logout_button_is_displayed()

        # check url
        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page or Login failed."


    @pytest.mark.tcid106
    def test_login_existing_user(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        login.valid_login()

        # check expected_text
        expected_message = GenericConfigs.LOGIN_SUCCESS_MSG 
        homepage.wait_until_success_message_is_displayed(expected_message)

        # check if logout bottun is displayed
        navigation.wait_until_logout_button_is_displayed()

        # check url
        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page or Login failed."

        