from selenium.webdriver.common.by import By
from locators.checkout import LocCheckout

class Checkout:
    def __init__(self, driver):
        self.driver = driver

    def input_firstname(self, first_name):
        self.driver.find_element(By.ID,LocCheckout.first_name).send_keys(first_name)

    def input_lastname(self,last_name):
        self.driver.find_element(By.ID,LocCheckout.last_name).send_keys(last_name)

    def input_zip(self,postal_code):
        self.driver.find_element(By.ID,LocCheckout.postal_code).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(By.ID,LocCheckout.continue_button).click()

    def message_login_error(self):
        error_checkout = self.driver.find_element(By.XPATH,LocCheckout.message_error_checkout)
        return error_checkout.text