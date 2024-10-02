from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10) 

driver.maximize_window()
'''
driver.get("https://demoqa.com/modal-dialogs")

driver.find_element(By.XPATH, "//button[@id='showLargeModal']").click()

try: 
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "//div[@id='example-modal-sizes-title-lg']")))
    modaltext = driver.find_element(By.ID, "//div[@id='example-modal-sizes-title-lg']").text
    print(modaltext)

except TimeoutException:
    print('element tidak muncul')
'''
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "alertButton").click()

try:
    WebDriverWait(driver,5).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

except TimeoutException:
    print("alert tidak muncul")

print(driver.find_element(By.XPATH, ""))
