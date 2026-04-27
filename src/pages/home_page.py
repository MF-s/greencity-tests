import allure
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class HomePage(BasePage):

    # Locators
    EVENTS_LINK = (By.XPATH, "//a[contains(@href, 'events')]")
    NEWS_LINK = (By.XPATH, "//a[contains(@href, 'news')]")
    MAP_LINK = (By.XPATH, "//a[contains(@href, 'places')]")
    ABOUT_LINK = (By.XPATH, "//a[contains(@href, 'about')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, 'profile')]")
    USB_LINK = (By.XPATH, "//a[contains(@href, 'usb')]")

    @allure.step("Go to Events page")
    def go_to_events(self):
        self.click(self.EVENTS_LINK)

    @allure.step("Go to News page")
    def go_to_news(self):
        self.click(self.NEWS_LINK)
        
    @allure.step("Go to Map page")
    def go_to_map(self):
        self.click(self.MAP_LINK)

    @allure.step("Go to About page")
    def go_to_about(self):
        self.click(self.ABOUT_LINK)

    @allure.step("Go to About page")
    def go_to_profile(self):
        self.click(self.PROFILE_LINK)

    @allure.step("Go to USB page")
    def go_to_usb(self):
        self.click(self.USB_LINK)