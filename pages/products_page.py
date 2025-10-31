from pages.base_page import BasePage
from pages.locators import products_locators as loc



class ProductsPage(BasePage):
    url_page = "/inventory.html"

    def check_count_products_is(self, count_products: int):
        product_list = self.find_all(loc.product_card)
        assert len(product_list) == count_products, f"Ожидалось {len(product_list)} товаров, найдено {count_products}"

    def check_add_buttons(self):
        buttons = self.find_all(loc.add_button)
        for button in buttons:
            button.click()
        cart = self.wait(loc.shopping_cart_number)
        assert int(cart.text) == len(buttons), (f"Количество товаров ожидалось – {len(buttons)}, "
                                                f"фактически – {cart.text}")

    def check_link_product(self):
        product = self.find(loc.product_card)
        product_text = product.find_element(*loc.product_name).text
        product.find_element(*loc.product_link).click()
        name_product_in_new_page = self.wait(loc.name_product_container)
        assert product_text == name_product_in_new_page.text
