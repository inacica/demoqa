from selenium.webdriver.common.by import By


class Locators:

    FULLNAME = (By.ID, 'userName')
    EMAIL = (By.ID, 'userEmail')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS =(By.ID, 'permanentAddress')
    SUBMIT_BUTTON = (By.ID, 'submit')
    HIGH = (By.XPATH, '//div[@id="output"]')

