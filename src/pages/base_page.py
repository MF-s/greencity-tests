import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    BASE_URL = "https://www.greencity.cx.ua/#/greenCity"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open base page")
    def open(self):
        self.driver.get(self.BASE_URL)

    @allure.step("Wait for element")
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Click element")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    @allure.step("Wait for multiple elements")
    def wait_for_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))