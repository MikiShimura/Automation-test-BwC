import pytest
from src.pages.RegisterPage import RegisterPage
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.pages.SitePostForm import SitePostForm
from src.pages.Alert import Alert
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
        alert = Alert(self.driver)

        login.valid_login()

        navigation.click_logout_button()

        expected_message = GenericConfigs.LOGOUT_SUCCESS_MSG 
        alert.wait_until_success_message_is_displayed(expected_message)

        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page or Logout failed."

        navigation.wait_until_login_button_is_displayed()
        
    @pytest.mark.tcid404
    def test_login_and_register_button_is_displayed_for_logged_in_user(self):
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        homepage.go_to_homepage()

        navigation.wait_until_login_button_is_displayed()
        navigation.wait_until_register_button_is_displayed()

    @pytest.mark.tcid405
    def test_click_login_button(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        homepage.go_to_homepage()
        navigation.click_login_button()

        current_url = self.driver.current_url
        expected_url = get_base_url() + login.endpoint

        assert current_url==expected_url, "Opened wrong page."

    @pytest.mark.tcid406
    def test_click_register_button(self):
        register = RegisterPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        homepage.go_to_homepage()
        navigation.click_register_button()

        current_url = self.driver.current_url
        expected_url = get_base_url() + register.endpoint

        assert current_url==expected_url, "Opened wrong page."

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
        alert = Alert(self.driver)

        login.valid_login(admin=True)

        expected_message = GenericConfigs.LOGIN_SUCCESS_MSG 
        alert.wait_until_success_message_is_displayed(expected_message)

        navigation.wait_until_post_button_is_displayed()

    @pytest.mark.tcid409
    def test_click_post_button(self):
        login = LoginPage(self.driver)
        site_post = SitePostForm(self.driver)
        navigation = NavigationBar(self.driver)

        login.valid_login(admin=True)
        navigation.click_post_new_site_button()

        current_url = self.driver.current_url
        expected_url = get_base_url() + site_post.endpoint

        assert current_url==expected_url, "Opened wrong page."

    @pytest.mark.tcid410
    def test_click_site_logo(self):
        login = LoginPage(self.driver)
        navigation = NavigationBar(self.driver)

        login.go_to_login()
        navigation.click_site_logo()

        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Opened wrong page."
