import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import wait_for_element

class TestEventsPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
    
    def tearDown(self):
        self.driver.quit()
    
    # TC1
    def test_events_cards_present(self):
        driver = self.driver

        event = wait_for_element(
            driver,
            By.XPATH,
            "//mat-card[contains(@class, 'event-list-item')]"
        )

        self.assertIsNotNone(event, "Події не знайдені на сторінці")

        events = driver.find_elements(
            By.XPATH,
            "//mat-card[contains(@class, 'event-list-item')]"
        )

        print(f"Знайдено {len(events)} подій")


    # TC2
    def test_open_event_details(self):
        driver = self.driver

        more_button = wait_for_element(
            driver,
            By.XPATH,
            "(//button[contains(., 'Більше')])[1]"
        )

        more_button.click()

        details = wait_for_element(
            driver,
            By.XPATH,
            "//div[contains(@class, 'description-block-title')]"
        )

        self.assertIsNotNone(details, "Сторінка деталей не відкрилась")

        print("Деталі події відкрито успішно")


    # TC3
    def test_search_events(self):
        driver = self.driver

        search_button = wait_for_element(
            driver,
            By.XPATH,
            "//span[contains(@class, 'search-img')]"
        )
        search_button.click()

        search_input = wait_for_element(
            driver,
            By.XPATH,
            "//input[contains(@placeholder, 'Search')]"
        )

        search_input.clear()
        search_input.send_keys("E")

        wait_for_element(
            driver,
            By.XPATH,
            "//mat-card[contains(@class, 'event-list-item')]"
        )

        events_after_E = driver.find_elements(
            By.XPATH,
            "//mat-card[contains(@class, 'event-list-item')]"
        )

        self.assertGreater(len(events_after_E), 0, "Немає результатів для 'E'")
        print(f"Результати для 'E': {len(events_after_E)}")

        search_input.clear()
        search_input.send_keys("Eco")

        events_after_Eco = driver.find_elements(
            By.XPATH,
            "//mat-card[contains(@class, 'event-list-item')]"
        )

        self.assertEqual(len(events_after_Eco), 0, "Очікувався баг, але результати є")

        print("БАГ підтверджено: для 'Eco' результатів немає")


    # TC4
    def test_invalid_url_error_message(self):
        driver = self.driver

        driver.get("https://www.greencity.cx.ua/#/greenCity/events/invalid-page")

        error_message = wait_for_element(
            driver,
            By.XPATH,
            "//div[contains(., 'Сталася помилка')]"
        )

        self.assertIsNotNone(error_message, "Повідомлення про помилку не з'явилось")

        print("Повідомлення про помилку з'явилось")


if __name__ == "__main__":
    unittest.main(verbosity=2)