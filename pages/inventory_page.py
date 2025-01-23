from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import time

class InventoryPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.filter_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_item_to_cart(self, item_name):
        item_xpath = f"//div[text()='{item_name}']/../../..//button"
        self.driver.find_element(By.XPATH, item_xpath).click()

    def sort_items(self, option):
        dropdown = self.driver.find_element(*self.filter_dropdown)
        dropdown.click()
        dropdown.find_element(By.XPATH, f"//option[text()='{option}']").click()    

    def get_cart_item_count(self):
        return self.driver.find_element(*self.cart_badge).text

    def add_items_to_cart(self, items):
        for item in items:
            self.add_item_to_cart(item)
            time.sleep(1)  

    def navigate_to_product_details(self, product_name):
      product_link = self.driver.find_element(By.XPATH, f"//*[text()='{product_name}']")
      product_link.click()
      time.sleep(2)

    def add_item_from_details_page(self):
        add_to_cart_button = self.driver.find_element(By.CLASS_NAME, "btn_inventory")
        add_to_cart_button.click()
        time.sleep(2)     

    def logout(self):
        menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        time.sleep(1)
        logout_link = self.driver.find_element(By.ID, "logout_sidebar_link")
        logout_link.click()
        assert "https://www.saucedemo.com/" in self.driver.current_url
        

        


