import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(20)
driver.minimize_window()

driver.get("https://demoqa.com/alerts")

driver.find_element(By.ID, "timerAlertButton").click()

try:
    WebDriverWait(driver, 15).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("Berhasil")

except TimeoutException:
    print("Gagal")
    pass


try:
    confirm_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "confirmButton"))).click()

    WebDriverWait(driver, 20).until(EC.alert_is_present())
    
    alert = driver.switch_to.alert
    action = alert.text
    if "Do you confirm action?" in action:
        alert.accept()
        print("You selected Ok")
    else:
        alert.dismiss()
        print("You selected Cancel")

except TimeoutException:
    print("Gagal")
    pass

try:
    prompt_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "promptButton"))).click()

    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Dandi Test Input")
    alert.accept()

    result_text = driver.find_element(By.ID, "promptResult").text
    print(result_text) 

except TimeoutException:
    print("Gagal")
    pass