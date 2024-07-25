import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.configs.generic_configs import GenericConfigs


@pytest.mark.usefixtures("init_driver")
class TestHomepageAdmin:

    @pytest.mark.tcid314
    def test_post_new_site_button_is_displayed(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        login.go_to_login()
        login.input_login_username(GenericConfigs.ADMIN["username"])
        login.input_login_password(GenericConfigs.ADMIN["password"])
        login.click_login_button()

        expected_message = GenericConfigs.LOGIN_SUCCESS_MSG 
        homepage.wait_until_success_message_is_displayed(expected_message)

        navigation.wait_until_post_button_is_displayed()