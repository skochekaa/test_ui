def test_correct_login(login_page):
    login_page.open_page()
    login_page.fill_login_form("standard_user", "secret_sauce")
    login_page.check_url("https://www.saucedemo.com/inventory.html")


def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form("standard_user", "secret_sauc")
    login_page.check_error_text_is("Epic sadface: Username and password do not match any user in this service")


def test_locked_out_user(login_page):
    login_page.open_page()
    login_page.fill_login_form("locked_out_user", "secret_sauce")
    login_page.check_error_text_is("Epic sadface: Sorry, this user has been locked out.")
