import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.SiteDetailedPage import SiteDetailedPage
from src.configs.generic_configs import GenericConfigs


@pytest.mark.usefixtures("init_driver")
class TestSiteDetailedPageContentDisplayed:

    @pytest.mark.tcid701
    def test_site_info_is_displayed(self):
        homepage = HomePage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        homepage.go_to_homepage()
        homepage.click_random_site()

        sdp.wait_until_all_the_site_info_is_displayed()
    
    @pytest.mark.tcid703
    def test_site_reviews_are_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        sdp.wait_until_reviews_are_displayed()

    @pytest.mark.tcid704
    def test_site_review_label_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        sdp.wait_until_review_label_are_displayed("Reviews")

    @pytest.mark.tcid705
    def test_site_no_reviews_label_is_displayed(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.SITE_WITHOUT_REVIEW_URL)

        sdp.wait_until_review_label_are_displayed("No reviews")

    @pytest.mark.tcid706
    def test_contents_are_displayed_on_review(self):
        sdp = SiteDetailedPage(self.driver)

        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        sdp.wait_until_star_is_displayed()
        sdp.wait_until_comment_is_displayed()
        sdp.wait_until_username_is_displayed()

    @pytest.mark.tcid707
    def test_post_review_button_is_not_displayed(self):
        homepage = HomePage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        homepage.go_to_homepage()
        homepage.click_random_site()

        sdp.wait_until_open_review_form_button_is_not_displayed()

    @pytest.mark.tcid708
    def test_post_review_button_is_displayed_for_registered_user(self):
        homepage = HomePage(self.driver)
        login = LoginPage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        login.valid_login()
        homepage.go_to_homepage()
        homepage.click_random_site()

        sdp.wait_until_open_review_form_button_is_displayed()

    @pytest.mark.tcid711
    def test_review_form_label_is_displayed_on_post_review_form(self):
        login = LoginPage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        login.valid_login()
        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        sdp.click_open_review_form_button()
        sdp.wait_until_review_form_label_is_displayed("Post review")

    @pytest.mark.tcid712
    def test_stars_are_selectable_on_post_review_form(self):
        login = LoginPage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        login.valid_login()
        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        sdp.click_open_review_form_button()
        sdp.wait_until_star_is_displayed()
        star_to_be_selected = 4
        sdp.choose_star(star_to_be_selected)
        sdp.star_is_selected(star_to_be_selected)

    @pytest.mark.tcid713
    def test_post_review_button_is_displayed_on_post_review_form(self):
        login = LoginPage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        login.valid_login()
        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)

        sdp.click_open_review_form_button()
        sdp.wait_until_post_review_button_is_displayed("Post review")

    @pytest.mark.tcid714
    def test_delete_review_button_is_displayed(self):
        login = LoginPage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        # Login as Miki
        login.valid_login()
        self.driver.get(GenericConfigs.SITE_WITH_REVIEW_URL)
        sdp.post_new_review()

        # search reviews whose username is "Miki" and return index
        reviews = sdp.get_all_reviews()
        list = [sdp.get_review_username(review) for review in reviews]
        index_of_specified_user_review = [i for i, x in enumerate(list) if x == "Miki"]
                
        # check if reviews[index] has buttons in roop
        for n in index_of_specified_user_review:
            sdp.delete_review_button_is_displayed(reviews[n])

    @pytest.mark.tcid716
    def test_edit_site_button_is_not_displayed(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        login.valid_login()

        homepage.go_to_homepage()
        homepage.click_random_site()

        sdp.wait_until_edit_site_button_is_not_displayed()

    @pytest.mark.tcid717
    def test_edit_site_button_is_displayed_for_admin(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        login.valid_login(admin=True)

        homepage.go_to_homepage()
        homepage.click_random_site()

        sdp.wait_until_edit_site_button_is_displayed()

    @pytest.mark.tcid718
    def test_delete_site_button_is_not_displayed(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        login.valid_login()

        homepage.go_to_homepage()
        homepage.click_random_site()

        sdp.wait_until_delete_site_button_is_not_displayed()

    @pytest.mark.tcid719
    def test_delete_site_button_is_displayed_for_admin(self):
        login = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        sdp = SiteDetailedPage(self.driver)

        login.valid_login(admin=True)

        homepage.go_to_homepage()
        homepage.click_random_site()

        sdp.wait_until_delete_site_button_is_displayed()