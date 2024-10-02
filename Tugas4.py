from selenium import webdriver

url_list = [
    'https://tiket.com',
    'https://tokopedia.com',
    'https://orangsiber.com',
    'https://demoqa.com',
    'https://automatetheboringstuff.com'
]

driver = webdriver.Chrome()
driver.minimize_window()

for url in url_list:
    driver.get(url)
    Title = driver.title
    Name = url.replace('https://','')
    print(Name,'-',Title)

driver.close()