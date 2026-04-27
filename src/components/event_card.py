import allure
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent


class EventCard(BaseComponent):

    TITLE = (By.XPATH, ".//h2")
    MORE_BUTTON = (By.XPATH, ".//button[contains(., 'Більше')]")

    @allure.step("Get event title")
    def get_title(self):
        return self.find(self.TITLE).text

    @allure.step("Click 'More' button in event card")
    def click_more(self):
        self.click(self.MORE_BUTTON)