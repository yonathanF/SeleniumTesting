# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class RegTestCaseSuccessful(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_reg_test_case_successful(self):
        driver = self.driver
        driver.get(self.base_url + "/motivational/register")
        self.assertEqual("", driver.title)
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys("Atoshem")
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys("Gheb")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("123@gmail.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()
        self.assertEqual("", driver.title)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
