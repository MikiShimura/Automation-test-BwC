import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.SearchSection import SearchSection
from src.pages.MainMap import MainMap
from src.pages.SiteDetailedPage import SiteDetailedPage
from src.configs.generic_configs import GenericConfigs


@pytest.mark.usefixtures("init_driver")
class TestSiteDetailedPageContentDisplayed:

    @pytest.mark.tcid701
    def test_site_info_is_displayed(self):
        homepage = HomePage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        homepage.go_to_homepage()
        homepage.click_random_site()

        sdp.wait_until_all_the_site_info_is_displayed()
    
    @pytest.mark.tcid703
    def test_site_reviews_are_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        sdp.wait_until_reviews_are_displayed()

    @pytest.mark.tcid704
    def test_site_review_label_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        sdp.wait_until_review_label_are_displayed("Reviews")

    @pytest.mark.tcid705
    def test_site_no_reviews_label_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_review_label_are_displayed("No reviews")

    @pytest.mark.tcid706
    def test_contents_are_displayed_on_review(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        sdp.wait_until_star_is_displayed()
        sdp.wait_until_comment_is_displayed()
        sdp.wait_until_username_is_displayed()

    @pytest.mark.tcid707
    def test_post_review_button_is_not_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_post_review_button_is_not_displayed()

    @pytest.mark.tcid708
    def test_post_review_button_is_displayed_for_logined_user(self):
        login = LoginPage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        login.valid_login()
        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_post_review_button_is_displayed()