import pytest
from src.pages.LoginPage import LoginPage
from src.pages.RegisterPage import RegisterPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.pages.SitePostForm import SitePostForm
from src.pages.SiteDetailedPage import SiteDetailedPage
from src.pages.Alert import Alert
from src.configs.generic_configs import GenericConfigs
from src.helpers.config_helpers import get_base_url

@pytest.mark.usefixtures("init_driver")
class TestEditDeleteSitesPositive:
    
    @pytest.mark.tcid721
    def test_delete_site(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)
        sdp = SiteDetailedPage(self.driver)
        alert = Alert(self.driver)

        login.valid_login(admin=True)

        # create site first
        navigation.click_post_new_site_button()
        site_post.post_new_site(ages=2)

        homepage.go_to_homepage()
        number_of_site_before = len(homepage.get_all_sites())
        homepage.click_site(number_of_site_before)

        sdp.click_delete_site_button()

        expected_message = GenericConfigs.SITE_DELETE_MSG
        alert.wait_until_success_message_is_displayed(expected_message)

        current_url = self.driver.current_url
        expected_url = get_base_url()

        assert current_url==expected_url, "Redirected to wrong page."

        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before - 1 == number_of_site_after, "Site is not deleted on homepage"

        # homepage.go_to_homepage()
        # homepage.click_site(8)