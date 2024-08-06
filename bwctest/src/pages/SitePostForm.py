from src.SeleniumExtended import SeleniumExtended
from src.pages.locators.SitePostFormLocators import SitePostFormLocators
import os
from selenium.common.exceptions import ElementNotInteractableException
import time

class SitePostForm(SitePostFormLocators):

    endpoint = "new"

    site_default = {"title":"test", "description":"test", "category":"Culture", "ages":2, 
                    "location":"test", "longtitude":"1.111", "latitude":"1.111", 
                    "url":"test.com", "price":"300", "uproad":True}

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_site_title(self, title=site_default["title"]):
        self.sl.wait_and_input_text(self.TITLE_FIELD, title)

    def input_site_description(self, description=site_default["description"]):
        self.sl.wait_and_input_text(self.DESCRIPTION_FIELD, description)

    def choose_site_category(self, category=site_default["category"]):
        if category == "Culture":
            self.sl.wait_and_click(self.CATEGORY_RADIO_CULTURE)
        elif category == "Sport":
            self.sl.wait_and_click(self.CATEGORY_RADIO_SPORT)
        elif category == "Entertainment":
            self.sl.wait_and_click(self.CATEGORY_RADIO_ENTERTAINMENT)
        elif category == "Nature":
            self.sl.wait_and_click(self.CATEGORY_RADIO_NATURE)
        elif category == "Education":
            self.sl.wait_and_click(self.CATEGORY_RADIO_EDUCATION)

    def choose_site_ages(self, ages=site_default["ages"]):
        checkboxes = [self.AGES_CHECKBOX_0_1, self.AGES_CHECKBOX_2_3, self.AGES_CHECKBOX_4_6, self.AGES_CHECKBOX_7_9, self.AGES_CHECKBOX_10]
        if ages > 5:
            print("Argument of function 'choose_site_ages' should be lower than 6")
        for n in range(ages): 
            self.sl.wait_and_click(checkboxes[n])
    
    def input_site_location(self, location=site_default["location"]):
        self.sl.wait_and_input_text(self.LOCATION_FIELD, location)

    def input_site_longtitude(self, longtitude=site_default["longtitude"]):
        self.sl.wait_and_input_text(self.LONGTITUDE_FIELD, longtitude)

    def input_site_latitude(self, latitude=site_default["latitude"]):
        self.sl.wait_and_input_text(self.LATITUDE_FIELD, latitude)

    def input_site_url(self, url=site_default["url"]):
        self.sl.wait_and_input_text(self.URL_FIELD, url)

    def input_site_price(self, price=site_default["price"]):
        self.sl.wait_and_input_text(self.PRICE_FIELD, price)

    def uproad_site_image(self, uproad=True):
        if uproad:
            image_path = os.getcwd() + '\\test1.jpg' 
            elm = self.sl.wait_and_get_elements(self.IMG_UPROAD_BTN)[0]
            elm.send_keys(image_path)

    def click_done_button(self):
        try: 
            self.sl.wait_and_click(self.DONE_BTN)
        except ElementNotInteractableException: 
            time.sleep(2)
            self.sl.wait_and_click(self.DONE_BTN)
    
    def post_new_site(self, title=site_default["title"], description=site_default["description"], 
                      category=site_default["category"], ages=site_default["ages"], 
                      location=site_default["location"], longtitude=site_default["longtitude"], 
                      latitude=site_default["latitude"], url=site_default["url"], 
                      price=site_default["price"], uproad=site_default["uproad"]):
        self.input_site_title(title=title)
        self.input_site_description(description=description)
        self.choose_site_category(category=category)
        self.choose_site_ages(ages=ages)
        self.input_site_location(location=location)
        self.input_site_longtitude(longtitude=longtitude)
        self.input_site_latitude(latitude=latitude)
        self.input_site_url(url=url)
        self.input_site_price(price=price)
        self.uproad_site_image(uproad=uproad)
        self.click_done_button()
        
    def title_invalid_alert_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.INVALID_ALERT_TITLE)

    def description_invalid_alert_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.INVALID_ALERT_DESCRIPTION)
    
    def location_invalid_alert_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.INVALID_ALERT_LOCATION)

    def longtitude_invalid_alert_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.INVALID_ALERT_LONGTITUDE)

    def latitude_invalid_alert_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.INVALID_ALERT_LATITUDE)

    def price_invalid_alert_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.INVALID_ALERT_PRICE)
        