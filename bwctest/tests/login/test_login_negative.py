import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.configs.generic_configs import GenericConfigs


@pytest.mark.usefixtures("init_driver")
class TestLoginPositive:

    @pytest.mark.tcid104
    def test_login_invaild_admin_username(self):
        login = LoginPage(self.driver)

        login.go_to_login()
        login.input_login_username("John")
        login.input_login_password(GenericConfigs.ADMIN_PASS)
        login.click_login_button()

        expected_error = GenericConfigs.LOGIN_INVAILD_CREDENCIAL_ERR_MSG
        login.wait_until_error_message_is_displayed(expected_error)

    @pytest.mark.tcid105
    def test_login_invaild_admin_username(self):
        login = LoginPage(self.driver)

        login.go_to_login()
        login.input_login_username(GenericConfigs.ADMIN_NAME)
        login.input_login_password("1234")
        login.click_login_button()

        expected_error = GenericConfigs.LOGIN_INVAILD_CREDENCIAL_ERR_MSG
        login.wait_until_error_message_is_displayed(expected_error)
    