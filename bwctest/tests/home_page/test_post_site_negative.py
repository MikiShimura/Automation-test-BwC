import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.pages.SitePostForm import SitePostForm
from src.configs.generic_configs import GenericConfigs
from src.helpers.config_helpers import get_base_url


@pytest.mark.usefixtures("init_driver")
class TestPostSiteNegative:

    @pytest.mark.tcid319
    def test_post_new_site_without_title(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(title="")

        site_post.invalid_alert_is_displayed()

        homepage.go_to_homepage()
        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before == number_of_site_after, "Site with invalid info shouldn't be added on homepage"