import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.configs.generic_configs import GenericConfigs
from src.helpers.config_helpers import get_base_url


@pytest.mark.usefixtures("init_driver")
class TestContentDisplayed:

    @pytest.mark.tcid402
    def test_logout_button_is_displayed_for_logged_in_user(self):
        login = LoginPage(self.driver)
        navigation = NavigationBar(self.driver)

        login.valid_login()

        navigation.wait_until_logout_button_is_displayed()

    @pytest.mark.tcid403
    def test_click_logout_button(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        login.valid_login()

        navigation.click_logout_button()

        expected_message = GenericConfigs.LOGOUT_SUCCESS_MSG 
        homepage.wait_until_success_message_is_displayed(expected_message)

        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page or Logout failed."

        navigation.wait_until_login_button_is_displayed()

    @pytest.mark.tcid407
    def test_post_new_site_button_is_not_displayed(self):
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        homepage.go_to_homepage()

        navigation.wait_until_post_button_is_not_displayed()

    @pytest.mark.tcid408
    def test_post_new_site_button_is_displayed_for_admin(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        login.valid_login(admin=True)

        expected_message = GenericConfigs.LOGIN_SUCCESS_MSG 
        homepage.wait_until_success_message_is_displayed(expected_message)

        navigation.wait_until_post_button_is_displayed()
