from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

def test_login_positive():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.get('https://saucedemo.com')
    #proses login
    driver.find_element(By.ID,'user-name').send_keys('standard_user')
    driver.find_element(By.ID,'password').send_keys('secret_sauce')
    driver.find_element(By.ID,'login-button').click()

    #product page
    title = driver.find_element(By.XPATH,"//span[@class='title']").text

    #assertion
    assert title == 'Products'

    driver.close()

#def test_login_without_username():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.get('https://saucedemo.com')
    #proses login
    driver.find_element(By.ID,'password').send_keys('secret_sauce')
    driver.find_element(By.ID,'login-button').click()

    #product page
    error = driver.find_element(By.XPATH,"//div[@class='error-message-container error']").text

    #assertion
    assert error == 'Epic sadface: Username is required'

    driver.close()
    
#def test_login_wrongpassword():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.get('https://saucedemo.com')
    #proses login
    driver.find_element(By.ID,'user-name').send_keys('standard_user')
    driver.find_element(By.ID,'password').send_keys('secret_sauces')
    driver.find_element(By.ID,'login-button').click()

    #product page
    error2 = driver.find_element(By.XPATH,"//div[@class='error-message-container error']").text

    #assertion
    assert error2 == 'Epic sadface: Username and password do not match any user in this service'

    driver.close()

error_sample = [('standard_user','salah','Epic sadface: Username and password do not match any user in this service'),
                ('locked_out_user','secret_sauce','Epic sadface: Sorry, this user has been locked out.'),
                ('salah','secret_sauce','Epic sadface: Username and password do not match any user in this service'),
                ('','secret_sauce','Epic sadface: Username is required')]

@pytest.mark.parametrize('username,password,error_message',error_sample)
def test_login_error(username,password,error_message):
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.get('https://saucedemo.com')
    #proses login
    driver.find_element(By.ID,'user-name').send_keys(username)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()

    #product page
    error2 = driver.find_element(By.XPATH,"//div[@class='error-message-container error']").text

    #assertion
    assert error2 == error_message

    driver.close()
