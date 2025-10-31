from pages.base_page import BasePage
from pages.locators import login_locators as loc


class LoginPage(BasePage):

    def check_error_text_is(self, text):
        error_alert = self.find(loc.error)
        assert error_alert.text == text
