import time
import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_add_items_to_cart(setup):
    login_page = LoginPage(setup)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    print(f"Current URL after login: {setup.current_url}")
    assert "inventory.html" in setup.current_url

    inventory_page = InventoryPage(setup)
    inventory_page.sort_items("Price (low to high)")
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    inventory_page.add_items_to_cart(items_to_add)

    cart_item_count = inventory_page.get_cart_item_count()
    print(f"Cart item count: {cart_item_count}")
    assert cart_item_count == "2"

    cart_page = CartPage(setup)
    cart_page.go_to_cart()

    for item in items_to_add:
        item_in_cart = cart_page.is_item_in_cart(item)
        assert item_in_cart, f"Item {item} was not found in the cart"
    print("Test Passed: Items added to cart successfully.")

