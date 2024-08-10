import pytest
from src.pages.RegisterPage import RegisterPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.pages.Alert import Alert
from src.helpers.generic_helpers import generate_random_username_email_and_password
from src.helpers.config_helpers import get_base_url


@pytest.mark.usefixtures("init_driver")
class TestRegisterPositive:
    @pytest.mark.tcid203
    def test_resister_new_user(self):
        register = RegisterPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        alert = Alert(self.driver)

        register.go_to_register()
        rand_info = generate_random_username_email_and_password()
        register.input_register_username(rand_info["username"])
        register.input_register_email(rand_info["email"])
        register.input_register_password(rand_info["password"])
        register.click_register_button()

        expected_message = "Welcome!"
        alert.wait_until_success_message_is_displayed(expected_message)

        navigation.wait_until_logout_button_is_displayed()

        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page or Resister failed."
