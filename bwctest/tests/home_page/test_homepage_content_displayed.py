import pytest
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.pages.SearchSection import SearchSection
from src.pages.SiteDetailedPage import SiteDetailedPage


@pytest.mark.usefixtures("init_driver")
class TestHomepageContentDisplayed:

    @pytest.mark.tcid301
    def test_navigation_is_displayed_on_top(self):
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        homepage.go_to_homepage()

        navigation.wait_until_nav_bar_is_displayed()

        navigation = navigation.get_nav_element()
        navigation_location = navigation.location
        assert navigation_location['y'] == 0, "Navigation should be displayed top"

    @pytest.mark.tcid302
    def test_app_image_is_displayed_under_navigation(self):
        homepage = HomePage(self.driver)
        navigation = NavigationBar(self.driver)

        homepage.go_to_homepage()

        navigation.wait_until_nav_bar_is_displayed()
        homepage.wait_until_app_image_is_displayed()

        navigation = navigation.get_nav_element()
        navigation_location = navigation.location
        app_image = homepage.get_app_image_element()
        app_image_location = app_image.location
        assert navigation_location['y'] < app_image_location['y'], "App image should be displayed under navigation"

    @pytest.mark.tcid303
    def test_search_section_is_displayed_on_left(self):
        pass

    @pytest.mark.tcid304
    def test_map_is_displayed_under_app_image(self):
        homepage = HomePage(self.driver)

        homepage.go_to_homepage()

        homepage.wait_until_app_image_is_displayed()
        homepage.wait_until_map_is_displayed()

        app_image = homepage.get_app_image_element()
        app_image_location = app_image.location
        map = homepage.get_map_element()
        map_location = map.location
        
        assert app_image_location['y'] < map_location['y'], "Map should be displayed under app image"

    @pytest.mark.tcid305
    def test_sites_are_displayed_under_map(self):
        homepage = HomePage(self.driver)

        homepage.go_to_homepage()

        homepage.wait_until_map_is_displayed()
        homepage.wait_until_sites_section_is_displayed()

        map = homepage.get_map_element()
        map_location = map.location
        sites = homepage.get_sites_section_element()
        sites_location = sites.location
        
        assert map_location['y'] < sites_location['y'], "Sites should be displayed under map"

    @pytest.mark.tcid306
    def test_site_infomation_is_displayed_in_each_site_card(self):
        homepage = HomePage(self.driver)
        
        homepage.go_to_homepage()

        all_sites = homepage.get_all_sites()
        for n in range(len(all_sites)):
            homepage.wait_until_site_image_is_displayed(all_sites[n])
            homepage.wait_until_site_title_is_displayed(all_sites[n])
            # homepage.wait_until_site_category_is_displayed(all_sites[n])
            # homepage.wait_until_site_ages_are_displayed(all_sites[n])

    @pytest.mark.tcid312
    def test_click_any_site(self):
        homepage = HomePage(self.driver)
        sdp = SiteDetailedPage(self.driver)
        
        homepage.go_to_homepage()
        number_of_chosen_site = homepage.click_random_site()

        site_title_adp = sdp.get_site_title_text()

        homepage.go_to_homepage()
        all_sites = homepage.get_all_sites()
        site_title_homepage = homepage.get_site_title(all_sites[number_of_chosen_site-1])

        assert site_title_adp == site_title_homepage, "Site on homepage link to different site detailed page"

    @pytest.mark.tcid318
    def test_search_result_message_is_displayed(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()

        # Scroll down 500px so that Selenium elements can be interactable
        self.driver.execute_script("window.scrollTo(0, 500)")

        search.choose_categories_on_seach_section()
        search.choose_ages_on_seach_section()
        search.click_search_button()

        number_of_site = len(homepage.get_all_sites())
        if number_of_site == 0:
            displayed_msg = homepage.wait_until_search_result_text_is_displayed()
            expected_msg = "No result"

            assert displayed_msg == expected_msg, "Search result message is wrong"
        else:
            displayed_msg = homepage.wait_until_search_result_text_is_displayed()
            expected_msg = f"{number_of_site}sites found"

            assert displayed_msg == expected_msg, "Search result message is wrong"