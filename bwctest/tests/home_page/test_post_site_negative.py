import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.pages.SitePostForm import SitePostForm


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

        site_post.title_invalid_alert_is_displayed()

        homepage.go_to_homepage()
        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before == number_of_site_after, "Site with invalid info shouldn't be added on homepage"

    @pytest.mark.tcid320
    def test_post_new_site_without_description(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(description="")

        site_post.description_invalid_alert_is_displayed()

        homepage.go_to_homepage()
        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before == number_of_site_after, "Site with invalid info shouldn't be added on homepage"

    @pytest.mark.tcid323
    def test_post_new_site_without_location(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(location="")

        site_post.location_invalid_alert_is_displayed()

        homepage.go_to_homepage()
        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before == number_of_site_after, "Site with invalid info shouldn't be added on homepage"

    @pytest.mark.tcid324
    def test_post_new_site_without_longtitude(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(longtitude="")

        site_post.longtitude_invalid_alert_is_displayed()

        homepage.go_to_homepage()
        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before == number_of_site_after, "Site with invalid info shouldn't be added on homepage"

    @pytest.mark.tcid325
    def test_post_new_site_without_latitude(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(latitude="")

        site_post.latitude_invalid_alert_is_displayed()

        homepage.go_to_homepage()
        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before == number_of_site_after, "Site with invalid info shouldn't be added on homepage"
    
    @pytest.mark.tcid326
    def test_post_new_site_without_price(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(price="")

        site_post.price_invalid_alert_is_displayed()

        homepage.go_to_homepage()
        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before == number_of_site_after, "Site with invalid info shouldn't be added on homepage"

    @pytest.mark.tcid327
    def test_post_new_site_with_price_in_letter(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(price="three hundred")

        site_post.price_invalid_alert_is_displayed()

        homepage.go_to_homepage()
        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before == number_of_site_after, "Site with invalid info shouldn't be added on homepage"
    
    @pytest.mark.skip(reason="This crush homepage and can't access any page")
    @pytest.mark.tcid328
    def test_post_new_site_without_image(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)
        site_post = SitePostForm(self.driver)

        login.valid_login(admin=True)

        number_of_site_before = len(homepage.get_all_sites())

        navigation.click_post_new_site_button()
        site_post.post_new_site(uproad=False)

        site_post.price_invalid_alert_is_displayed()

        homepage.go_to_homepage()
        number_of_site_after = len(homepage.get_all_sites())
        assert number_of_site_before == number_of_site_after, "Site with invalid info shouldn't be added on homepage"