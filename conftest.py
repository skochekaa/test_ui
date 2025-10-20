from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.login_page import LoginPage
import time


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    time.sleep(3)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)
