from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
import time


# Setup Chrome dengan opsi untuk tetap terbuka
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Membuka Chrome dengan opsi
driver = webdriver.Chrome(options=options)

# Navigasi ke halaman login
driver.get("https://management-staging.kopikenangan.com/")
driver.implicitly_wait(10)
driver.minimize_window()

# Cetak judul halaman
print("Page Title:", driver.title)

# Login
username = "dandi.setiawan"
password = "@Dandistw11"

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
driver.find_element(By.XPATH, "//body/app-root[1]/div[1]/nz-layout[1]/app-login[1]/div[1]/div[2]/form[1]/nz-form-item[3]/nz-form-control[1]/div[1]/div[1]/button[1]").click()

driver.find_element(By.XPATH,"//span[contains(text(),'Promotion Management')]").click()
driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/nz-layout[1]/nz-sider[1]/div[1]/ul[1]/li[6]/div[2]/ul[1]/li[3]/a[1]").click()
driver.find_element(By.XPATH,"//span[contains(text(),'Create New Voucher')]").click()

#Scenario
driver.find_element(By.XPATH,"//div[@id='scenario']//label[1]//span[1]//input[1]").click()
#Availability
driver.find_element(By.XPATH,"//input[@value='1003']").click()
#Promotion
driver.find_element(By.XPATH,"//div[@id='promotion_type']//label[1]//span[2]").click()
#Display name
driver.find_element(By.ID,"name").send_keys("TestAuto")
#campaign name
driver.find_element(By.ID,"campaign_name").send_keys("TestAuto1")
#detail
driver.find_element(By.ID,"detail").send_keys("Testautodetail")
#voucher purpose
driver.find_element(By.XPATH,"//input[@value='4001']").click()

#lowest value
driver.find_element(By.XPATH,"//span[@class='ant-radio ant-radio-checked']//input[@value='false']").click()

#Discount Type
driver.find_element(By.XPATH,"//div[@id='discount_type']//input[@value='1']").click()

# Open the discount dropdown
discount_dropdown = driver.find_element(By.XPATH, "//span[@title='%']")
discount_dropdown.click()

# Select IDR option from the dropdown
idr_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'IDR')]"))
)
idr_option.click()

# Fill in the discount value and minimum transaction
driver.find_element(By.ID,"discount_value").send_keys("5000")
driver.find_element(By.ID,"minimum_transaction").send_keys("15000")
driver.find_element(By.XPATH,"//div[@id='before_or_after_discount']//input[@value='2']").click()

# Get the current date and time, and add 5 minutes
current_datetime = datetime.now()
new_datetime = current_datetime + timedelta(minutes=5)
formatted_datetime = new_datetime.strftime("%d-%b-%Y %H:%M:%S")

#distribution time using current datetime + 5 minutes
driver.find_element(By.XPATH, "//input[@id='distribution_time']").click()
driver.find_element(By.XPATH, "//input[@id='distribution_time']").send_keys(formatted_datetime)
driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-sm']").click()

# # Usage time "From"
driver.find_element(By.XPATH, "//input[@id='usage_from']").click()
driver.find_element(By.XPATH, "//input[@id='usage_from']").send_keys(formatted_datetime)

ok_button = driver.find_element(By.XPATH, "(//span[contains(text(),'Ok')])[2]")
print("Displayed:", ok_button.is_displayed())
print("Enabled:", ok_button.is_enabled())

# If enabled and displayed, click it
if ok_button.is_enabled() and ok_button.is_displayed():
    ok_button.click()
else:
    print("The OK button is not ready to be clicked.")

# # Wait for the "OK" button to be clickable
# ok_button = WebDriverWait(driver, 50).until(
#     EC.element_to_be_clickable((By.XPATH, "(//button[@class='ant-btn ant-btn-primary ant-btn-sm'])[1]"))
# )

# driver.execute_script("arguments[0].click();", ok_button)


# Usage time "To"
driver.find_element(By.XPATH, "//input[@id='usage_end']").click()
driver.find_element(By.XPATH, "//input[@id='usage_end']").send_keys("30-Sep-2024 18:12:20")

# Ensure the OK button is clickable for "Usage To"
ok_button_usage_to = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Ok')])[3]"))
)
ok_button_usage_to.click()

# Quantity
driver.find_element(By.XPATH, "//input[@id='quantity']").send_keys("1000000")
#Allowed to be used on discounte product
driver.find_element(By.XPATH, "//div[@id='allow_on_discount_product']//input[@value='true']").click()
#User
driver.find_element(By.XPATH, "//span[@class='ant-radio']//input[@value='1003']").click()

#Upload Voucher Image

# Locate the input element for uploading the image (assuming it's of type 'file')
#driver.find_element(By.XPATH, "//body/app-root[@class='root']/div[@class='ng-star-inserted']/nz-layout[@class='app-layout ant-layout ant-layout-has-sider ng-star-inserted']/nz-layout[@class='ant-layout']/nz-content[@class='ant-layout-content']/div[@class='inner-content']/react-adapter[@class='ng-star-inserted']/div/section[@class='ant-layout layout']/main[@class='ant-layout-content info-page-voucher']/form[@class='ant-form ant-form-horizontal ant-form-hide-required-mark ant-form-small form']/div[@class='ant-card card ant-card-bordered ant-card-small ant-card-type-inner']/div[@class='ant-card-body']/div[@class='ant-row ant-form-item no-margin10 no-required upload-template']/div[@class='ant-col ant-col-19 ant-form-item-control']/div[@class='ant-form-item-control-input']/div[@class='ant-form-item-control-input-content']/div[@class='ant-row ant-form-item no-margin']/div[@class='ant-col ant-form-item-control']/div[@class='ant-form-item-control-input']/div[@class='ant-form-item-control-input-content']/span[@class='upload-list-inline']/div[@class='ant-upload ant-upload-select ant-upload-select-picture']/span[@role='button']/button[@type='button']/span[1]").click()

# Locate the input element for uploading the image (adjust the XPath if necessary)
file_input = driver.find_element(By.XPATH, "//input[@type='file']")

# Path to the image you want to upload
image_path = "C:/Users/dandi.setiawan/Downloads/rose-7687604_1280.png"

# Upload the file by sending the file path directly to the input element
file_input.send_keys(image_path)

# Wait for a moment to allow the file upload process
time.sleep(5)

#driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
