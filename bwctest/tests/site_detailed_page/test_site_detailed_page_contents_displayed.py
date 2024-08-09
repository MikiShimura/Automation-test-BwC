import pytest
from src.pages.HomePage import HomePage
from src.pages.SearchSection import SearchSection
from src.pages.MainMap import MainMap
from src.pages.SiteDetailedPage import SiteDetailedPage
from src.configs.generic_configs import GenericConfigs


@pytest.mark.usefixtures("init_driver")
class TestSiteDetailedPageContentDisplayed:

    @pytest.mark.tcid701
    def test_site_title_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)
        # homepage.go_to_homepage()
        # homepage.click_random_site()

        sdp.wait_until_title_is_displayed()

    @pytest.mark.tcid702
    def test_site_image_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_image_is_displayed()