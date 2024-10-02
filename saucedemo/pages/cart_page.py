from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.cart import LocCart

class Cart:
    def __init__(self, driver):
        self.driver = driver

    # Method to go to the cart page
    def go_to_cart(self):
        # Explicit wait to ensure the cart link is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LocCart.cart_link))
        ).click()

    # Method to get the cart item count
    def get_cart_item_count(self):
        return self.driver.find_element(By.XPATH, LocCart.cart_badge).text

    # Method to click the checkout button
    def click_checkout_button(self):
        self.driver.find_element(By.ID, LocCart.checkout_button).click()
