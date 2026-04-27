import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseComponent:

    def __init__(self, driver, root=None):
        self.driver = driver
        self.root = root
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Find element inside component")
    def find(self, locator):
        if self.root:
            return self.root.find_element(*locator)
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Find elements inside component")
    def find_all(self, locator):
        if self.root:
            return self.root.find_elements(*locator)
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Click element inside component")
    def click(self, locator):
        if self.root:
            self.root.find_element(*locator).click()
        else:
            self.wait.until(EC.element_to_be_clickable(locator)).click()