import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar
from src.pages.SearchSection import SearchSection
from src.configs.generic_configs import GenericConfigs


@pytest.mark.usefixtures("init_driver")
class TestSearchContentDisplayed:

    @pytest.mark.tcid501
    def test_correct_category_labels_are_displayed(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()
        search.wait_until_category_labels_are_displayed("Culture", "Sport", "Entertainment", "Nature", "Education")

    @pytest.mark.tcid502
    def test_correct_age_labels_are_displayed(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()
        
        search.wait_until_age_labels_are_displayed("0~1 yrs", "2~3 yrs", "4~6 yrs", "7~9 yrs", "10~ yrs")

    @pytest.mark.tcid503
    def test_search_button_is_displayed(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()
        
        search.wait_until_search_button_displayed("Search")

    @pytest.mark.tcid504
    def test_clear_all_button_is_displayed(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()
        
        search.wait_until_clear_all_button_displayed("Clear all")

    @pytest.mark.tcid505
    def test_click_clear_all_button(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()

        self.driver.execute_script("window.scrollTo(0, 500)")

        search.choose_categories_on_seach_section(5)
        search.choose_ages_on_seach_section(5)
        search.click_clear_all_button()

        assert search.categories_are_not_selected() == True, "All the category checkboxes should be unselected."
        assert search.ages_are_not_selected() == True, "All the age checkboxes should be unselected."

    @pytest.mark.tcid506
    def test_search_with_a_category(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()

        number_of_all_site = len(homepage.get_all_sites())

        self.driver.execute_script("window.scrollTo(0, 500)")

        search.choose_categories_on_seach_section(1)
        search.click_search_button()

        number_of_searched_site = len(homepage.get_all_sites())
        assert number_of_all_site > number_of_searched_site, "Number of searched sites result should be less than all the sites"

    @pytest.mark.tcid507
    def test_search_with_two_categories(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()

        number_of_all_site = len(homepage.get_all_sites())

        self.driver.execute_script("window.scrollTo(0, 500)")

        search.choose_categories_on_seach_section(2)
        search.click_search_button()

        number_of_searched_site = len(homepage.get_all_sites())
        assert number_of_all_site > number_of_searched_site, "Number of searched sites result should be less than all the sites"

    @pytest.mark.tcid508
    def test_search_with_a_age(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()

        number_of_all_site = len(homepage.get_all_sites())

        self.driver.execute_script("window.scrollTo(0, 500)")

        search.choose_ages_on_seach_section(1)
        search.click_search_button()

        number_of_searched_site = len(homepage.get_all_sites())
        assert number_of_all_site > number_of_searched_site, "Number of searched sites result should be less than all the sites"

    @pytest.mark.tcid509
    def test_search_with_two_ages(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()

        number_of_all_site = len(homepage.get_all_sites())

        self.driver.execute_script("window.scrollTo(0, 500)")

        search.choose_ages_on_seach_section(2)
        search.click_search_button()

        number_of_searched_site = len(homepage.get_all_sites())
        assert number_of_all_site < number_of_searched_site, "Number of searched sites result should be less than all the sites"


    @pytest.mark.tcid510
    def test_search_with_a_category_and_a_age(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()

        number_of_all_site = len(homepage.get_all_sites())

        self.driver.execute_script("window.scrollTo(0, 500)")

        search.choose_categories_on_seach_section(1)
        search.choose_ages_on_seach_section(1)
        search.click_search_button()

        number_of_searched_site = len(homepage.get_all_sites())
        assert number_of_all_site > number_of_searched_site, "Number of searched sites result should be less than all the sites"

    @pytest.mark.tcid511
    def test_search_with_all_checkboxes_empty(self):
        homepage = HomePage(self.driver)
        search = SearchSection(self.driver)

        homepage.go_to_homepage()

        number_of_all_site = len(homepage.get_all_sites())

        self.driver.execute_script("window.scrollTo(0, 500)")

        search.click_clear_all_button()

        number_of_searched_site = len(homepage.get_all_sites())
        assert number_of_all_site == number_of_searched_site, "Number of searched sites result should be same as all the sites"