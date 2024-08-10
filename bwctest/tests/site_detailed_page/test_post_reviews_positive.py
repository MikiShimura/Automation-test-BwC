import pytest
from src.pages.LoginPage import LoginPage
from src.pages.SiteDetailedPage import SiteDetailedPage
from src.configs.generic_configs import GenericConfigs
import time


@pytest.mark.usefixtures("init_driver")
class TestPostReviewsPositive:

    @pytest.mark.tcid709
    def test_post_new_review_as_registered_user(self):
        login = LoginPage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        login.valid_login()
        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sdp.post_review()