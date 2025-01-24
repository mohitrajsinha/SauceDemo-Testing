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

@pytest.mark.run(order=6)
def test_remove_item_from_cart(setup):
    # Login to the application
    login_page = LoginPage(setup)
    login_page.login(VALID_USERNAME, VALID_PASSWORD) 
    print(f"Current URL after login: {setup.current_url}")
    assert "inventory.html" in setup.current_url

    inventory_page = InventoryPage(setup)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bike Light")
    inventory_page.add_item_to_cart("Sauce Labs Onesie")
    assert inventory_page.get_cart_item_count() == "3"

    cart_page = CartPage(setup)
    cart_page.go_to_cart()

    removed_item_name = cart_page.remove_item_by_price_range(8, 10)

    cart_count = inventory_page.get_cart_item_count()
    print(f"Cart count after removal: {cart_count}")
    assert cart_count == "2", f"Cart count should be 2 but was {cart_count}"

    item_in_cart = cart_page.is_item_in_cart(removed_item_name)
    assert not item_in_cart, f"Item '{removed_item_name}' was not removed from the cart"
    print(f"Test Passed: Item '{removed_item_name}' removed successfully.")
