import pytest
from src.pages.HomePage import HomePage
from src.pages.SearchSection import SearchSection
from src.pages.MainMap import MainMap
from src.pages.SiteDetailedPage import SiteDetailedPage
from src.configs.generic_configs import GenericConfigs
from src.helpers.config_helpers import get_base_url


@pytest.mark.usefixtures("init_driver")
class TestMainMapContentDisplayed:

    @pytest.mark.tcid601
    def test_pins_are_displayed_on_main_map(self):
        homepage = HomePage(self.driver)
        map = MainMap(self.driver)

        homepage.go_to_homepage()

        map.wait_until_pins_are_displayed()

    @pytest.mark.tcid602
    def test_click_a_pin(self):
        homepage = HomePage(self.driver)
        map = MainMap(self.driver)

        homepage.go_to_homepage()

        # click pin of first site
        map.click_pin()
        map.wait_until_popup_is_displayed()

    @pytest.mark.tcid603
    def test_click_link_on_popup(self):
        homepage = HomePage(self.driver)
        map = MainMap(self.driver)
        sdp = SiteDetailedPage(self.driver)

        homepage.go_to_homepage()

        map.click_pin()
        site_title_on_popup = map.get_link_text_on_popup()

        map.click_link_on_popup()
        site_title_on_sdp = sdp.get_site_title_text()

        assert site_title_on_popup == site_title_on_sdp, "Link on popup on map leads wrong page"

    @pytest.mark.tcid604
    def test_click_close_button_on_popup(self):
        homepage = HomePage(self.driver)
        map = MainMap(self.driver)

        homepage.go_to_homepage()

        map.click_pin()
        map.wait_until_popup_is_displayed()

        map.click_close_button_on_popup()
        map.wait_until_popup_is_not_displayed()

    @pytest.mark.tcid605
    def test_seached_result_is_displayed_on_map(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)
        map = MainMap(self.driver)

        homepage.go_to_homepage()
        
        self.driver.execute_script("window.scrollTo(0, 500)")

        search.choose_categories_on_seach_section(2)
        search.click_search_button()

        number_of_seach_result_sites = len(homepage.get_all_sites())

        map.click_zoom_out()
        number_of_sites_on_map = len(map.get_pins())

        assert number_of_seach_result_sites == number_of_sites_on_map, "Search result on map and the one on homepage is not same."