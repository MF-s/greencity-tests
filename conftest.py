import pytest
import allure
from selenium import webdriver
from src.pages.home_page import HomePage

@pytest.fixture
def driver():
    with allure.step("Start browser"):
        driver = webdriver.Chrome()
        driver.maximize_window()
    yield driver
    with allure.step("Close browser"):
        driver.quit()

@pytest.fixture
def home_page(driver):
    with allure.step("Open GreenCity Home Page"):
        page = HomePage(driver)
    page.open()
    return page