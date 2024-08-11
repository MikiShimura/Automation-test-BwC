import pytest
from src.pages.LoginPage import LoginPage
from src.pages.SiteDetailedPage import SiteDetailedPage
from src.pages.Alert import Alert
from src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
class TestPostDeleteReviewsPositive:

    @pytest.mark.tcid709
    def test_post_new_review_as_registered_user(self):
        login = LoginPage(self.driver)
        sdp = SiteDetailedPage(self.driver)
        alert = Alert(self.driver)

        login.valid_login()
        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        number_of_reviews_before = len(sdp.get_all_reviews())
        sdp.post_new_review()

        expected_message = GenericConfigs.NEW_REVIEW_POST_MSG
        alert.wait_until_success_message_is_displayed(expected_message)

        number_of_reviews_after = len(sdp.get_all_reviews())
        assert number_of_reviews_before + 1 == number_of_reviews_after, "Review is not added on site detailed page."

    @pytest.mark.tcid715
    def test_delete_my_review(self):
        login = LoginPage(self.driver)
        sdp = SiteDetailedPage(self.driver)
        alert = Alert(self.driver)

        login.valid_login()
        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        sdp.post_new_review()

        number_of_reviews_before = len(sdp.get_all_reviews())
        sdp.click_delete_button_of_latest_review(number_of_reviews_before)

        expected_message = GenericConfigs.REVIEW_DELETE_MSG
        alert.wait_until_success_message_is_displayed(expected_message)

        number_of_reviews_after = len(sdp.get_all_reviews())
        assert number_of_reviews_before - 1 == number_of_reviews_after, "Review is not deleted on site detailed page"
