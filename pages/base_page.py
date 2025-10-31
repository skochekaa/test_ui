from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import login_locators as loc


class BasePage:
    home_page = "https://www.saucedemo.com"
    url_page = None

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def open_page(self, page=None):
        if page:
            self.driver.get(f"{self.home_page}{page}")
        elif self.home_page:
            self.driver.get(self.home_page)
        else:
            raise NotImplementedError("Нет такой страниц для данного класса")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def fill_login_form(self, user_name: str, password: str):
        login_field = self.find(loc.user_name)
        pass_field = self.find(loc.password)
        login_button = self.find(loc.button_login)
        login_field.send_keys(user_name)
        pass_field.send_keys(password)
        login_button.click()

    def check_title(self, locators, text):
        self.driver.implicitly_wait(5)
        title = self.find(*locators)
        assert title.text == text

    def check_url(self, page: str):
        self.driver.implicitly_wait(3)
        url = self.driver.current_url
        assert url == page

    def wait(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не найден"
        )
