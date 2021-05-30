from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testData import TestData
from locators import Locators
import time


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def enter_userdata(self):
        self.click(Locators.FULLNAME)
        self.enter_text(Locators.FULLNAME, TestData.NAME)
        self.click(Locators.EMAIL)
        self.enter_text(Locators.EMAIL, TestData.EMAIL)
        self.click(Locators.CURRENT_ADDRESS)
        self.enter_text(Locators.CURRENT_ADDRESS, TestData.CURRENT_ADDRESS)
        self.click(Locators.PERMANENT_ADDRESS)
        self.enter_text(Locators.PERMANENT_ADDRESS, TestData.PERMANENT_ADDRESS)
        time.sleep(1)

    def submit(self):
        self.click(Locators.SUBMIT_BUTTON)
