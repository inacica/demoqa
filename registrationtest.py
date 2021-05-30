import json
import unittest
from selenium import webdriver
from pages import HomePage
from highlighting import highlight
from testData import TestData


class TestRegistrationBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(TestData.BASE_URL)
        self.driver.implicitly_wait(5)

    def test_register_validation(self):
        self.homePage = HomePage(self.driver)
        self.homePage.enter_userdata()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.homePage.submit()

        text_result = self.driver.find_element_by_xpath('//div[@id="output"]')
        highlight(text_result)

        with open("Output.txt", "w") as text_file:
            text_file.write(text_result.text)

        file_dict = {}
        with open("Output.txt") as f:
            for line in f:
                (key, val) = line.rstrip('\n').split(':')
                file_dict[key] = val
        print(file_dict)

        with open("testData.json") as j:
            string = j.read()
            data_dict = json.loads(string)
        print(data_dict)

        self.assertDictEqual(file_dict, data_dict)


if __name__ == "__main__":
    unittest.main()