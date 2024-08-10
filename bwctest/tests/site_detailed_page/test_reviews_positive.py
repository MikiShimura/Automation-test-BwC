import pytest
from src.pages.HomePage import HomePage
from src.pages.SiteDetailedPage import SiteDetailedPage


@pytest.mark.usefixtures("init_driver")
class TestReviewsPositive:

    @pytest.mark.tcid709
    def test_post_new_review_as_registered_user(self):
        pass