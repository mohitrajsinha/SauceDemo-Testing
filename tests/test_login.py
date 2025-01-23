import time
import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_valid_login(setup):
    login_page = LoginPage(setup)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    print(f"Current URL after login: {setup.current_url}") 
    assert "inventory.html" in setup.current_url

def test_invalid_login(setup):
    login_page = LoginPage(setup)
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service"
    
def test_empty_credentials(setup):
    login_page = LoginPage(setup)
    login_page.login("", "")
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username is required"    
