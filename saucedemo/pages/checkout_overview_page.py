from selenium.webdriver.common.by import By
from locators.co_overview import LocOverview

class Overview:
    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        self.driver.find_element(By.ID, LocOverview.finish_button).click()

    def get_confirmation_message(self):
        return self.driver.find_element(By.XPATH,LocOverview.confirmation_message).text
