import pytest
from src.pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestHomepageContentDisplayed:

    @pytest.mark.tcid301
    def test_navigation_is_displayed_on_top(self):
        homepage = HomePage(self.driver)

        homepage.go_to_homepage()

        homepage.wait_until_navigation_is_displayed()

        navigation = homepage.get_navigation_element()
        navigation_location = navigation.location
        assert navigation_location['y'] == 0, "Navigation should be displayed top"

    @pytest.mark.tcid302
    def test_app_image_is_displayed_under_navigation(self):
        homepage = HomePage(self.driver)

        homepage.go_to_homepage()

        homepage.wait_until_navigation_is_displayed()
        homepage.wait_until_app_image_is_displayed()

        navigation = homepage.get_navigation_element()
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
    def test_site_image_is_displayed_in_each_site_card(self):
        homepage = HomePage(self.driver)
        
        homepage.go_to_homepage()

        all_sites = homepage.get_all_sites()
        for n in range(len(all_sites)):
            homepage.get_site_image(all_sites[n])
    
    @pytest.mark.tcid307
    def test_site_title_is_displayed_in_each_site_card(self):
        homepage = HomePage(self.driver)
        
        homepage.go_to_homepage()

        all_sites = homepage.get_all_sites()
        for n in range(len(all_sites)):
            homepage.get_site_title(all_sites[n])
    
    @pytest.mark.tcid308
    def test_site_categories_are_displayed_in_each_site_card(self):
        homepage = HomePage(self.driver)
        
        homepage.go_to_homepage()

        all_sites = homepage.get_all_sites()
        for n in range(len(all_sites)):
            homepage.get_site_categories(all_sites[n])

    @pytest.mark.tcid309
    def test_site_ages_are_displayed_in_each_site_card(self):
        homepage = HomePage(self.driver)
        
        homepage.go_to_homepage()

        all_sites = homepage.get_all_sites()
        for n in range(len(all_sites)):
            homepage.get_site_ages(all_sites[n])