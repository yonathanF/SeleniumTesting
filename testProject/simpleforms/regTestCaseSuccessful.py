from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from django.test import LiveServerTestCase


class LoginTestCase(LiveServerTestCase):
    fixtures=['fixture.json']
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = self.live_server_url
        self.verificationErrors = []
        self.accept_next_alert = True

    def fill_reg_form(self):
        driver = self.driver
        driver.get(self.base_url + "/motivational/register")
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys("Atoshem")
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys("Gheb")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("123@gmail.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()

    def test_login_successful(self):
        driver = self.driver
        self.fill_reg_form()
        
        driver.get(self.base_url + "/motivational/login")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("123@gmail.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()        
        
        self.assertTrue("Welcome Atoshem Gheb" in driver.page_source)
    
    def test_login_account_DNE(self):
        driver = self.driver
                
        driver.get(self.base_url + "/motivational/login")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("123@gmail.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()        
        
        self.assertTrue("Can't find that account. Try again please." in driver.page_source)
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class RegiserTestCase(LiveServerTestCase):
    fixtures=['fixture.json']
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = self.live_server_url
        self.verificationErrors = []
        self.accept_next_alert = True

    def fill_reg_form(self):
        driver = self.driver
        driver.get(self.base_url + "/motivational/register")
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys("Atoshem")
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys("Gheb")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("123@gmail.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()
        

    def test_reg_successful(self):
        driver = self.driver
        self.fill_reg_form()
        self.assertTrue("Welcome Atoshem Gheb" in driver.page_source)

    def test_reg_account_exists(self):
        driver = self.driver
        self.fill_reg_form()
        
        driver.back()

        self.fill_reg_form()
        self.assertTrue("Try again with a different email" in driver.page_source)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
