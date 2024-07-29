import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.pages.SitePostForm import SitePostForm
from src.configs.generic_configs import GenericConfigs
from src.helpers.config_helpers import get_base_url


@pytest.mark.usefixtures("init_driver")
class TestHomepageAdmin:

    @pytest.mark.tcid314
    def test_post_new_site_button_is_displayed(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        login.valid_login(admin=True)

        expected_message = GenericConfigs.LOGIN_SUCCESS_MSG 
        homepage.wait_until_success_message_is_displayed(expected_message)

        navigation.wait_until_post_button_is_displayed()

    @pytest.mark.tcid315
    def test_post_new_site(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(ages=1)

        expected_message = GenericConfigs.NEW_SITE_POST_MSG
        homepage.wait_until_success_message_is_displayed(expected_message)

        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page."

        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before + 1 == number_of_site_after, "Site is not added on homepage"
    
    @pytest.mark.tcid316
    def test_post_new_site_with_two_ages(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(ages=2)

        expected_message = GenericConfigs.NEW_SITE_POST_MSG
        homepage.wait_until_success_message_is_displayed(expected_message)

        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page."

        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before + 1 == number_of_site_after, "Site is not added on homepage"
    
    @pytest.mark.tcid317
    def test_post_new_site_without_url(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(ages=2, url="")

        expected_message = GenericConfigs.NEW_SITE_POST_MSG
        homepage.wait_until_success_message_is_displayed(expected_message)

        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page."

        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before + 1 == number_of_site_after, "Site is not added on homepage"