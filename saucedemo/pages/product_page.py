from selenium.webdriver.common.by import By
from locators.product import LocProd

class Product:
    def __init__(self,driver):
        self.driver = driver

    def check_title(self):
        title = self.driver.find_element(By.XPATH,LocProd.title_text).text
        return title
