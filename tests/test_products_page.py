def test_count_products(products_page):
    products_page.open_page()
    products_page.fill_login_form("standard_user", "secret_sauce")
    products_page.check_count_products_is(6)


def test_add_buttons(products_page):
    products_page.open_page()
    products_page.fill_login_form("standard_user", "secret_sauce")
    products_page.check_add_buttons()


def test_container_product_correct(products_page):
    products_page.open_page()
    products_page.fill_login_form("standard_user", "secret_sauce")
    products_page.check_link_product()
