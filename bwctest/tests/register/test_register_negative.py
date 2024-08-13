import pytest
from src.pages.RegisterPage import RegisterPage
from src.pages.Alert import Alert
from src.configs.generic_configs import GenericConfigs
from src.helpers.generic_helpers import generate_random_username_email_and_password


@pytest.mark.usefixtures("init_driver")
class TestRegisterNegative:
    @pytest.mark.tcid204
    def test_register_empty_username(self):
        register = RegisterPage(self.driver)
        alert = Alert(self.driver)

        register.go_to_register()
        rand_info = generate_random_username_email_and_password()
        register.input_register_username("")
        register.input_register_email(rand_info["email"])
        register.input_register_password(rand_info["password"])
        register.click_register_button()

        expected_error = GenericConfigs.REGISTER_EMPTY_USERNAME_ERR_MSG
        alert.wait_until_error_message_is_displayed(expected_error)

    @pytest.mark.tcid205
    def test_register_empty_email(self):
        register = RegisterPage(self.driver)
        alert = Alert(self.driver)

        register.go_to_register()
        rand_info = generate_random_username_email_and_password()
        register.input_register_username(rand_info["username"])
        register.input_register_email("")
        register.input_register_password(rand_info["password"])
        register.click_register_button()

        expected_error = GenericConfigs.REGISTER_EMPTY_EMAIL_ERR_MSG
        alert.wait_until_error_message_is_displayed(expected_error)

    @pytest.mark.tcid206
    def test_register_invalid_email(self):
        register = RegisterPage(self.driver)
        alert = Alert(self.driver)

        register.go_to_register()
        rand_info = generate_random_username_email_and_password()
        register.input_register_username(rand_info["username"])
        register.input_register_email("aaaa") # without @ and domain#
        register.input_register_password(rand_info["password"])
        register.click_register_button()

        expected_error = GenericConfigs.REGISTER_INVALID_EMAIL_ERR_MSG
        alert.wait_until_error_message_is_displayed(expected_error)

    @pytest.mark.tcid207
    def test_register_empty_password(self):
        register = RegisterPage(self.driver)
        alert = Alert(self.driver)

        register.go_to_register()
        rand_info = generate_random_username_email_and_password()
        register.input_register_username(rand_info["username"])
        register.input_register_email(rand_info["email"])
        register.input_register_password("")
        register.click_register_button()

        expected_error = GenericConfigs.REGISTER_EMPTY_PASSWORD_ERR_MSG
        alert.wait_until_error_message_is_displayed(expected_error)
    
    @pytest.mark.tcid208
    def test_register_existing_username(self):
        register = RegisterPage(self.driver)
        alert = Alert(self.driver)

        register.go_to_register()
        rand_info = generate_random_username_email_and_password()
        register.input_register_username(GenericConfigs.VALID_USER["username"])
        register.input_register_email(rand_info["email"])
        register.input_register_password(rand_info["password"])
        register.click_register_button()

        expected_error = GenericConfigs.REGISTER_EXIST_USERNAME_ERR_MSG
        alert.wait_until_error_message_is_displayed(expected_error)

    @pytest.mark.tcid209
    def test_register_existing_email(self):
            register = RegisterPage(self.driver)
            alert = Alert(self.driver)

            register.go_to_register()
            rand_info = generate_random_username_email_and_password()
            register.input_register_username(rand_info["username"])
            register.input_register_email(GenericConfigs.VALID_USER["email"])
            register.input_register_password(rand_info["password"])
            register.click_register_button()

            expected_error = GenericConfigs.REGISTER_EXIST_EMAIL_ERR_MSG
            alert.wait_until_error_message_is_displayed(expected_error)
