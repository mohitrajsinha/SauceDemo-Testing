from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def click(self, by, locator):
        element = self.wait_for_element(by, locator)
        element.click()

    def enter_text(self, by, locator, text):
        element = self.wait_for_element(by, locator)
        element.send_keys(text)