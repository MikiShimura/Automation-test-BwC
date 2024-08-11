import pytest
from src.pages.LoginPage import LoginPage
from src.pages.SiteDetailedPage import SiteDetailedPage
from src.pages.Alert import Alert
from src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
class TestPostDeleteReviewsNegative:

    @pytest.mark.tcid710
    def test_post_new_review_without_comment(self):
        login = LoginPage(self.driver)
        sdp = SiteDetailedPage(self.driver)
        alert = Alert(self.driver)

        login.valid_login()
        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        number_of_reviews_before = len(sdp.get_all_reviews())
        sdp.post_new_review(comment="")

        sdp.comment_invalid_alert_is_displayed()

        number_of_reviews_after = len(sdp.get_all_reviews())
        assert number_of_reviews_before == number_of_reviews_after, "Review with invalid info shouldn't be added on site detailed page."

