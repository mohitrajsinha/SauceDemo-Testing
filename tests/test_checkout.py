import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.constants import BASE_URL, VALID_PASSWORD, VALID_USERNAME
from utils.driver_factory import get_driver


@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_checkout(setup):
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

    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(setup)

    checkout_page.fill_checkout_form("John", "Doe", "12345")

    checkout_page.continue_checkout()

    checkout_page.finish_checkout()

    checkout_page.get_success_message()

