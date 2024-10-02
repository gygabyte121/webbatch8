from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Chrome
driver = webdriver.Chrome()
# Open URL
driver.get('https://demoqa.com/webtables')

# Data
datas = [
    {'firstName': 'Dandi', 'lastName': 'Setiawan', 'userEmail': 'dandi@gmail.com', 'age': '20', 'salary': '1000', 'department': 'IT'},
    {'firstName': 'Zulfa', 'lastName': 'Dinda', 'userEmail': 'dinda@gmail.com', 'age': '21', 'salary': '2000', 'department': 'Finance'},
    {'firstName': 'Andi', 'lastName': 'Nugroho', 'userEmail': 'andi@gmail.com', 'age': '22', 'salary': '3000', 'department': 'Marketing'}
]

# Iterate over data
for data in datas:
    # Tunggu tombol 'Add' tersedia dan klik
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'addNewRecordButton'))
    )
    add_button.click()

    # Isi form
    for key, value in data.items():
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, key))
        )
        input_field.send_keys(value)

    # Klik tombol submit setelah form diisi
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'submit'))
    )
    submit_button.click()

# Close the browser
# driver.quit()
