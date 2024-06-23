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