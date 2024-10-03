import unittest
from distutils.command.register import register

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class UnitTest(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def test_SearchEngine(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_Search(self):
        self.driver.get("https://www.amazon.in/")
        searchbox = self.driver.find_element(By.NAME, 'field-keywords')
        searchbox.send_keys("laptop")
        searchbox.submit()
        try:
            self.driver.find_element(By.CLASS_NAME,"a-size-medium a-color-base a-text-normal").click()
        except:
            print(NoSuchElementException)


    def test_Sign_In(self):
        self.driver.get("https://www.amazon.in/")
        self.driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
        sign_in = self.driver.find_element(By.ID,"ap_email")
        sign_in.send_keys("abcd@email.com")
        sign_in.submit()

    @classmethod
    def test_closeBrowser(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['--html=reports/test_report.html', '--self-contained-html'])