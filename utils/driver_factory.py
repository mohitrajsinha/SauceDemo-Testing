import time
from selenium import webdriver

from utils.constants import BASE_URL

def get_driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
