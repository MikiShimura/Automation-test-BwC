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
    
    @pytest.mark.tcid704
    def test_site_address_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_address_is_displayed()

    @pytest.mark.tcid705
    def test_site_description_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_description_is_displayed()

    @pytest.mark.tcid706
    def test_site_category_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_category_is_displayed()

    @pytest.mark.tcid707
    def test_site_ages_are_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_ages_are_displayed()

    @pytest.mark.tcid708
    def test_site_price_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_price_is_displayed()

    @pytest.mark.tcid709
    def test_site_url_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_url_is_displayed()

    @pytest.mark.tcid710
    def test_site_map_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.FIRST_SITE_URL)

        sdp.wait_until_map_is_displayed()