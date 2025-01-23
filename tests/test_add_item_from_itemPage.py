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

def test_add_item_from_inventory_item_page(setup):
    # Login to the application
    login_page = LoginPage(setup)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    print(f"Current URL after login: {setup.current_url}")
    assert "inventory.html" in setup.current_url

    inventory_page = InventoryPage(setup)
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    inventory_page.add_items_to_cart(items_to_add)
    time.sleep(2)

    # Navigate to product details page
    # inventory_page = InventoryPage(setup)
    inventory_page.navigate_to_product_details("Sauce Labs Onesie")
    time.sleep(2)

    # Add the item to the cart from the product details page
    inventory_page.add_item_from_details_page()

    # Verify the cart count reflects the updated number
    cart_item_count = inventory_page.get_cart_item_count()
    print(f"Cart item count after adding Sauce Labs Onesie: {cart_item_count}")
    assert cart_item_count == "3"

    # Navigate to the cart page to verify the item is present
    cart_page = CartPage(setup)
    cart_page.go_to_cart()
    item_in_cart = cart_page.is_item_in_cart("Sauce Labs Onesie")
    assert item_in_cart, "Item 'Sauce Labs Onesie' was not found in the cart"
    print("Test Passed: Sauce Labs Onesie added from the item details page successfully.")
