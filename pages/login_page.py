import time
from selenium import webdriver

from selenium.webdriver.common.by import By

from pages.base_page import BasePage



class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")

    def login(self, username, password):
        self.enter_text(*self.USERNAME_INPUT, username)
        self.enter_text(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)
        
    def get_error_message(self):
        return self.wait_for_element(*self.ERROR_MESSAGE).text    


