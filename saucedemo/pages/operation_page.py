from selenium.webdriver.common.by import By
from locators.operation import LocOperation

class Operation:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_id):
        self.driver.find_element(By.ID, product_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.XPATH, LocOperation.cart_link).click()

    def get_cart_item_count(self):
        return self.driver.find_element(By.XPATH, LocOperation.cart_badge).text

    def check_title(self):
        return self.driver.find_element(By.CLASS_NAME, LocOperation.title).text
