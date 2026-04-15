from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EventsPage(BasePage):

    # 🔹 Locators
    EVENT_CARDS = (By.XPATH, "//mat-card[contains(@class, 'event-list-item')]")
    MORE_BUTTON = (By.XPATH, "(//button[contains(., 'Більше')])[1]")
    DETAILS_TITLE = (By.XPATH, "//div[contains(@class, 'description-block-title')]")
    SEARCH_BUTTON = (By.XPATH, "//span[contains(@class, 'search-img')]")
    SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Search')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(., 'Сталася помилка')]")

    # 🔹 Actions / Methods

    def get_events(self):
        return self.wait_for_element(self.EVENT_CARDS)

    def get_all_events(self):
        return self.driver.find_elements(*self.EVENT_CARDS)

    def open_first_event(self):
        self.click(self.MORE_BUTTON)

    def is_event_details_opened(self):
        return self.wait_for_element(self.DETAILS_TITLE)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def enter_search_text(self, text):
        search_input = self.wait_for_element(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(text)

    def get_events_after_search(self):
        return self.driver.find_elements(*self.EVENT_CARDS)

    def open_invalid_page(self):
        self.driver.get(self.BASE_URL + "/events/invalid-page")

    def get_error_message(self):
        return self.wait_for_element(self.ERROR_MESSAGE)
    
    def wait_for_events(self):
        return self.wait_for_elements(self.EVENT_CARDS)