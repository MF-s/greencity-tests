from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    # Locators
    EVENTS_LINK = (By.XPATH, "//a[contains(@href, 'events')]")
    NEWS_LINK = (By.XPATH, "//a[contains(@href, 'news')]")
    MAP_LINK = (By.XPATH, "//a[contains(@href, 'places')]")
    ABOUT_LINK = (By.XPATH, "//a[contains(@href, 'about')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, 'profile')]")
    USB_LINK = (By.XPATH, "//a[contains(@href, 'usb')]")

    def go_to_events(self):
        self.click(self.EVENTS_LINK)

    def go_to_news(self):
        self.click(self.NEWS_LINK)
        
    def go_to_map(self):
        self.click(self.MAP_LINK)

    def go_to_about(self):
        self.click(self.ABOUT_LINK)

    def go_to_profile(self):
        self.click(self.PROFILE_LINK)

    def go_to_usb(self):
        self.click(self.USB_LINK)