from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.SiteDetailedPageLocators import SiteDetailedPageLocators

class SiteDetailedPage(SiteDetailedPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def get_site_title_text(self):
        return self.sl.wait_and_get_text(self.SITE_TITLE)
    
    def wait_until_title_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_TITLE)

    def wait_until_image_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_IMAGES)

    def wait_until_address_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_ADDRESS)

    def wait_until_description_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_DESCRIPTION)

    def wait_until_category_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_CATEGORY)

    def wait_until_ages_are_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_AGES)
    
    def wait_until_price_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_PRICE)

    def wait_until_url_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_URL)

    def wait_until_map_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_MAP)

    def wait_until_all_the_site_info_is_displayed(self):
        self.wait_until_title_is_displayed()
        self.wait_until_image_is_displayed()
        self.wait_until_address_is_displayed()
        self.wait_until_description_is_displayed()
        self.wait_until_category_is_displayed()
        self.wait_until_ages_are_displayed()
        self.wait_until_price_is_displayed()
        self.wait_until_url_is_displayed()
        self.wait_until_map_is_displayed()

    def wait_until_reviews_are_displayed(self):
        self.sl.wait_until_all_elements_are_visible(self.SITE_REVIEWS)

    def wait_until_review_label_are_displayed(self, exp_text):
        self.sl.wait_until_element_contains_text(self.REVIEW_LABEL, exp_text)

    def wait_until_star_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_MAP)

    def wait_until_comment_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_MAP)

    def wait_until_username_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SITE_MAP)

    def wait_until_post_review_button_is_not_displayed(self):
        self.sl.wait_until_element_is_invisible(self.POST_REVIEW_BTN)

    def wait_until_post_review_button_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.POST_REVIEW_BTN)