from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CLASS_NAME, "checkout_button")


    def go_to_cart(self):
        """Navigate to the cart page."""
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

    def get_cart_items(self):
        """Retrieve all cart items as a list of tuples (name, price)."""
        item_elements = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        items = []
        for item in item_elements:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = float(item.find_element(By.CLASS_NAME, "inventory_item_price").text.strip("$"))
            items.append((name, price))
        return items

    def remove_item_by_price_range(self, min_price, max_price):
        """Remove the first item within the given price range and return its name."""
        cart_items = self.get_cart_items()
        for name, price in cart_items:
            if min_price <= price <= max_price:
                remove_button = self.driver.find_element(By.XPATH, f"//div[text()='{name}']/ancestor::div[@class='cart_item']//button")
                remove_button.click()
                return name
        raise ValueError(f"No items found in the price range ${min_price} - ${max_price}")

    def is_item_in_cart(self, item_name):
        """Check if an item is present in the cart."""
        try:
            self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']")
            return True
        except:
            return False

    def go_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()