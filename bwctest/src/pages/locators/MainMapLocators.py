from selenium.webdriver.common.by import By

class MainMapLocators():
    PINS_ON_MAP = (By.CSS_SELECTOR, 'div.mapboxgl-marker')
    POPUP_ON_MAP = (By.CSS_SELECTOR, 'div.mapboxgl-popup-content')
    LINK_ON_POPUP = (By.CSS_SELECTOR, 'div.mapboxgl-popup-content a')
    CLOSE_BTN_ON_POPUP = (By.CSS_SELECTOR, 'button.mapboxgl-popup-close-button')
    ZOOM_OUT_BTN = (By.CSS_SELECTOR, 'button.mapboxgl-ctrl-zoom-out')