import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import Login
from pages.product_page import Product
from pages.operation_page import Operation
from pages.cart_page import Cart
from pages.checkout_page import Checkout
from data.login import Data
from data.login import DataError
from data.checkout import DataCheckout
from data.checkout import DataValidateError
from pages.checkout_overview_page import Overview
from data.product_cart import DataProduct

@pytest.fixture
def setup_teardown():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://saucedemo.com")
    
    yield driver
    driver.close()

def test_login_positive(setup_teardown):
    login = Login(setup_teardown)
    produk = Product(setup_teardown)

    login.input_username(Data.username)
    login.input_password(Data.password)
    login.click_login()
    
    title = produk.check_title()
    
    assert title == 'Products'

@pytest.mark.parametrize('username,password,error_message', DataError.error_sample) 
def test_login_error(setup_teardown, username, password, error_message):
    login = Login(setup_teardown)

    # Use the parameterized username and password from the test cases
    login.input_username(username)
    login.input_password(password)
    login.click_login()

    error = login.message_login_error()

    assert error == error_message


def test_cart_operations(setup_teardown):
    login = Login(setup_teardown)
    operation = Operation(setup_teardown)

    login.input_username(Data.username)
    login.input_password(Data.password)
    login.click_login()

    # Add products to the cart
    operation.add_product_to_cart(DataProduct.first_product)
    operation.add_product_to_cart(DataProduct.second_product)

    operation.go_to_cart()
    
    cart_number = operation.get_cart_item_count()
    
    assert cart_number == '2'
    
def test_your_cart(setup_teardown):
    login = Login(setup_teardown)
    operation = Operation(setup_teardown)
    cart = Cart(setup_teardown)

    login.input_username(Data.username)
    login.input_password(Data.password)
    login.click_login()

    # Add products to cart
    operation.add_product_to_cart(DataProduct.first_product)
    operation.add_product_to_cart(DataProduct.second_product)

    # Process to checkout
    cart.go_to_cart()

    cart.click_checkout_button()

def test_checkout(setup_teardown):
    test_your_cart(setup_teardown)
    checkout = Checkout(setup_teardown)
    
    checkout.input_firstname(DataCheckout.first_name)
    checkout.input_lastname(DataCheckout.last_name)
    checkout.input_zip(DataCheckout.postal_code)

    checkout.click_continue()
                            
@pytest.mark.parametrize('firstname,lastname,zip,validate_error', DataValidateError.validateError_sample)
def test_negative_checkout(setup_teardown,firstname,lastname,zip,validate_error):
    test_your_cart(setup_teardown)
    checkout = Checkout(setup_teardown)

    checkout.input_firstname(firstname)
    checkout.input_lastname(lastname)
    checkout.input_zip(zip)
    checkout.click_continue()

    error_message = checkout.message_login_error()

    assert error_message == validate_error


def test_checkout_overview(setup_teardown):
    test_checkout(setup_teardown)
    overview = Overview(setup_teardown)

    # Find and click button
    overview.click_finish()

    confirmation_message = overview.get_confirmation_message()
    
    # Assertion to verify the thank you message is displayed
    assert confirmation_message == 'Thank you for your order!'