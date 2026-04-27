import allure
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.components.event_card import EventCard


class EventsPage(BasePage):

    EVENT_CARDS = (By.XPATH, "//mat-card[contains(@class, 'event-list-item')]")
    DETAILS_TITLE = (By.XPATH, "//div[contains(@class, 'description-block-title')]")
    SEARCH_BUTTON = (By.XPATH, "//span[contains(@class, 'search-img')]")
    SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Search')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(., 'Сталася помилка')]")

    @allure.step("Get event cards as components")
    def get_event_cards(self):
        elements = self.wait_for_elements(self.EVENT_CARDS)
        return [EventCard(self.driver, el) for el in elements]

    @allure.step("Open first event via component")
    def open_first_event(self):
        cards = self.get_event_cards()
        cards[0].click_more()

    @allure.step("Check event details opened")
    def is_event_details_opened(self):
        return self.wait_for_element(self.DETAILS_TITLE)

    @allure.step("Click search button")
    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    @allure.step("Enter search text: {text}")
    def enter_search_text(self, text):
        input_field = self.wait_for_element(self.SEARCH_INPUT)
        input_field.clear()
        input_field.send_keys(text)

    @allure.step("Wait for events after search")
    def wait_for_events(self):
        return self.wait_for_elements(self.EVENT_CARDS)

    @allure.step("Open invalid page")
    def open_invalid_page(self):
        self.driver.get(self.BASE_URL + "/events/invalid-page")

    @allure.step("Get error message")
    def get_error_message(self):
        return self.wait_for_element(self.ERROR_MESSAGE)