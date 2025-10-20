from pages.base_page import BasePage
from pages.locators import login_locators as loc


class LoginPage(BasePage):

    def fill_login_form(self, user_name: str, password: str):
        login_field = self.find(loc.user_name)
        pass_field = self.find(loc.password)
        login_button = self.find(loc.button_login)
        login_field.send_keys(user_name)
        pass_field.send_keys(password)
        login_button.click()

    def check_error_text_is(self, text):
        error_alert = self.find(loc.error)
        assert error_alert.text == text

