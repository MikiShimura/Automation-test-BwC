from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.SiteDetailedPageLocators import SiteDetailedPageLocators
from selenium.common.exceptions import ElementNotInteractableException
import time
from selenium.webdriver.common.by import By

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

    def wait_until_open_review_form_button_is_not_displayed(self):
        self.sl.wait_until_element_is_invisible(self.OPEN_REVIEW_FORM_BTN)

    def wait_until_open_review_form_button_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.OPEN_REVIEW_FORM_BTN)

    def click_open_review_form_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            self.sl.wait_and_click(self.OPEN_REVIEW_FORM_BTN)
        except ElementNotInteractableException:
            time.sleep(2)
            self.sl.wait_and_click(self.OPEN_REVIEW_FORM_BTN)

    def choose_star(self, rating):
        if rating == 1:
            self.sl.wait_and_click(self.RATING_STAR_1)
        elif rating == 2:
            self.sl.wait_and_click(self.RATING_STAR_2)
        elif rating == 3:
            self.sl.wait_and_click(self.RATING_STAR_3)
        elif rating == 4:
            self.sl.wait_and_click(self.RATING_STAR_4)
        elif rating == 5:
            self.sl.wait_and_click(self.RATING_STAR_5)
        else:
            print("Choose stars from 1 to 5")

    def input_comment(self, comment):
        self.sl.wait_and_input_text(self.COMMENT_FIELD, comment)

    def click_post_review_button(self):
        self.sl.wait_and_click(self.POST_REVIEW_BTN)

    def post_new_review(self, comment="TestComment", rating=5):
        self.click_open_review_form_button()
        self.choose_star(rating=rating)
        self.input_comment(comment=comment)
        self.click_post_review_button()

    def star_is_selected(self, rating):
        if rating == 1:
            self.sl.wait_until_element_is_selected(self.RATING_STAR_SELECT_1)
        elif rating == 2:
            self.sl.wait_until_element_is_selected(self.RATING_STAR_SELECT_2)
        elif rating == 3:
            self.sl.wait_until_element_is_selected(self.RATING_STAR_SELECT_3)
        elif rating == 4:
            self.sl.wait_until_element_is_selected(self.RATING_STAR_SELECT_4)
        elif rating == 5:
            self.sl.wait_until_element_is_selected(self.RATING_STAR_SELECT_5)
        else:
            print("Choose stars from 1 to 5")

    def get_all_reviews(self):
        return self.sl.wait_and_get_elements(self.SITE_REVIEWS)
    
    def get_review_username(self, parent):
        return parent.find_element(self.USERNAME_ON_REVIEW[0], self.USERNAME_ON_REVIEW[1]).text
    
    def comment_invalid_alert_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.INVARID_ALERT_COMMENT)

    def wait_until_review_form_label_is_displayed(self, exp_text):
        self.sl.wait_until_element_contains_text(self.REVIEW_FORM_LABEL, exp_text)

    def wait_until_post_review_button_is_displayed(self, exp_text):
        self.sl.wait_until_element_contains_text(self.POST_REVIEW_BTN, exp_text)

    def delete_review_button_is_displayed(self, parent):
        parent.find_element(self.DELETE_REVIEW_BTN[0], self.DELETE_REVIEW_BTN[1])

    def click_delete_button_of_latest_review(self, number):
        try: 
            self.driver.find_element(By.XPATH, f'/html/body/main/div[4]/div[{number}]/div/form/button').click()
        except ElementNotInteractableException:
            time.sleep(2)
            self.driver.find_element(By.XPATH, f'/html/body/main/div[4]/div[{number}]/div/form/button').click()

    def wait_until_edit_site_button_is_not_displayed(self):
        self.sl.wait_until_element_is_invisible(self.EDIT_SITE_BTN)

    def wait_until_edit_site_button_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.EDIT_SITE_BTN)
    
    def click_edit_site_button(self):
        self.sl.wait_and_click(self.EDIT_SITE_BTN)

    def wait_until_delete_site_button_is_not_displayed(self):
        self.sl.wait_until_element_is_invisible(self.DELETE_SITE_BTN)

    def wait_until_delete_site_button_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.DELETE_SITE_BTN)

    def click_delete_site_button(self):
        self.sl.wait_and_click(self.DELETE_SITE_BTN)