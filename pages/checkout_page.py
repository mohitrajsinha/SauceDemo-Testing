from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.continue_button = (By.CLASS_NAME, "cart_button")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")



    def fill_checkout_form(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)

    def continue_checkout(self):
        self.driver.find_element(*self.continue_button).click()

    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text
