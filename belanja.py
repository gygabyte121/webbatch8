import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def setup_teardown():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    # Precondition
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://saucedemo.com")
    
    yield driver
    
    # Post condition
    driver.quit()

def test_login_positive(setup_teardown):
    # Perform login
    setup_teardown.find_element(By.ID, 'user-name').send_keys('standard_user')
    setup_teardown.find_element(By.ID, 'password').send_keys('secret_sauce')
    setup_teardown.find_element(By.ID, 'login-button').click()
    
    # Check that the user is on the Products page
    title = setup_teardown.find_element(By.XPATH, "//span[@class='title']").text
    assert title == 'Products'

def test_cart_operations(setup_teardown):
    # First, login
    test_login_positive(setup_teardown)
    
    # Add products to the cart
    setup_teardown.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    setup_teardown.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    
    # Navigate to cart and check the cart number
    setup_teardown.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    cart_number = setup_teardown.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
    assert cart_number == '2', f"Expected cart number to be 2, but found {cart_number}"
    
def test_your_cart(setup_teardown):
    # Login and add products to the cart
    test_login_positive(setup_teardown)

    # Proceed to checkout
    setup_teardown.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

    # Wait until checkout button is clickable and proceed to checkout
    WebDriverWait(setup_teardown, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # Final confirmation
    print("Checkout button clicked, proceeding to checkout.")

def test_checkout(setup_teardown):
    # Ensure you are logged in and on the cart page first
    test_your_cart(setup_teardown)
    
    setup_teardown.find_element(By.ID, "first-name").send_keys("dandi")
    setup_teardown.find_element(By.ID, "last-name").send_keys("setiawan")
    setup_teardown.find_element(By.ID, "postal-code").send_keys("12121")
    setup_teardown.find_element(By.ID, "continue").click()


validate_checkout = [('','setiawan','12121','Error: First Name is required'),
                     ('dandi','','12121','Error: Last Name is required'),
                     ('dandi','setiawan','','Error: Postal Code is required')]

@pytest.mark.parametrize('firstname,lastname,zip,validate_error', validate_checkout)
def test_validate_checkout(setup_teardown,firstname,lastname,zip,validate_error):
    test_your_cart(setup_teardown)

    setup_teardown.find_element(By.ID, "first-name").send_keys(firstname)
    setup_teardown.find_element(By.ID, "last-name").send_keys(lastname)
    setup_teardown.find_element(By.ID, "postal-code").send_keys(zip)
    setup_teardown.find_element(By.ID, "continue").click()

    validadateerror = setup_teardown.find_element(By.XPATH,"//div[@class='error-message-container error']").text

    assert validadateerror == validate_error


def test_checkout_overview(setup_teardown):
    # Ensure you are logged in and have proceeded to the checkout page first
    test_checkout(setup_teardown)

    # Find and click the 'Finish' button
    finish_button = setup_teardown.find_element(By.ID, 'finish').click()

    # Check that the user is on the Products page
    title = setup_teardown.find_element(By.XPATH, "//h2[normalize-space()='Thank you for your order!']").text
    assert title == 'Thank you for your order!'
