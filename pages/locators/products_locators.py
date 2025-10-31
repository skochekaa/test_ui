from selenium.webdriver.common.by import By

products_list = (By.CSS_SELECTOR, "[class='inventory_list']")
product_card = (By.CSS_SELECTOR, "[class='inventory_item']")
product_name = (By.CSS_SELECTOR, "[class='inventory_item_name ']")
product_link = (By.TAG_NAME, "a")
name_product_container = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
add_button = (By.XPATH, "//button[text()='Add to cart']")
remove_button = (By.XPATH, "//button[text()='Remove']")
shopping_cart_number = (By.CLASS_NAME, "shopping_cart_badge")
back_button = (By.ID, "back-to-products")
