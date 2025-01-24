import pytest

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

@pytest.mark.run(order=8)
def test_logout(setup):
    login_page = LoginPage(setup)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    print(f"Current URL after login: {setup.current_url}")
    assert "inventory.html" in setup.current_url

    inventory_page = InventoryPage(setup)
    inventory_page.logout()
   



