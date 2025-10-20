from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    home_page = "https://www.saucedemo.com/"
    url_page = None

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def open_page(self):
        if self.url_page:
            self.driver.get(f"{self.home_page}{self.url_page}")
        elif self.home_page:
            self.driver.get(self.home_page)
        else:
            raise NotImplementedError("Нет такой страниц для данного класса")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def check_title(self, locators, text):
        self.driver.implicitly_wait(5)
        title = self.find(*locators)
        assert title.text == text

    def check_url(self, page: str):
        self.driver.implicitly_wait(3)
        url = self.driver.current_url
        assert url == page
