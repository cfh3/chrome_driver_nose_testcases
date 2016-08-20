"""
To run the tests in this file do:
~/envs/selenium/bin/nosetests ~/PycharmProjects/ChromeDriver_test_1/aweber.py
"""

import time
import unittest
from selenium import webdriver


class AweberTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        cls.driver.implicitly_wait(30)

    def test_title(self):
        self.driver.get('https://www.aweber.com')
        self.assertEqual(self.driver.title, "Email Marketing | AWeber")
        time.sleep(5)

    def test_pricing(self):
        self.driver.get('https://www.aweber.com')
        menu_button = self.driver.find_element_by_css_selector("li.hamburger-button")
        menu_button.click()
        pricing_link = self.driver.find_element_by_link_text("Standard Pricing")
        pricing_link.click()
        time.sleep(5)

    def test_default_monthly(self):
        self.driver.get('https://www.aweber.com/order.htm')
        monthly_radio = self.driver.find_element_by_id("monthly")
        self.assertTrue(monthly_radio.is_selected())

    def test_search(self):
        self.driver.get('https://www.aweber.com/')
        search_input = self.driver.find_element_by_id("query")
        search_input.send_keys('Meet the Team')
        search_submit = self.driver.find_element_by_class_name("search-submit")
        search_submit.click()
        self.assertTrue(self.driver.find_element_by_link_text("AWeber Communications"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
