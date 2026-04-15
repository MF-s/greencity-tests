import pytest
from selenium import webdriver
from pages.home_page import HomePage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    page = HomePage(driver)
    page.open()
    return page