"""
To run the tests in this file do:
~/envs/selenium/bin/nosetests ~/PycharmProjects/ChromeDriver_test_1/aweber.py
"""

import time
import unittest
from selenium import webdriver


class ElementTestsClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        cls.driver.implicitly_wait(10)

    def test_title(self):
        self.driver.get('https://the-internet.herokuapp.com/')
        self.assertEqual(self.driver.title, "The Internet")
        time.sleep(5)

    def test_floating_menu(self):
        self.driver.get('https://the-internet.herokuapp.com/floating_menu')
        menu_button = self.driver.find_element_by_css_selector("#menu > ul > li:nth-child(1) > a")
        menu_button.click()
        # pricing_link = self.driver.find_element_by_link_text("Standard Pricing")
        # pricing_link.click()
        time.sleep(5)

    def test_default_monthly(self):
        self.driver.get('https://the-internet.herokuapp.com/')
        monthly_radio = self.driver.find_element_by_id("monthly")
        self.assertFalse(monthly_radio.is_selected())

    def test_search(self):
        self.driver.get('https://the-internet.herokuapp.com/')
        search_input = self.driver.find_element_by_id("query")
        search_input.send_keys('Meet the Team')
        search_submit = self.driver.find_element_by_class_name("search-submit")
        search_submit.click()
        self.assertTrue(self.driver.find_element_by_link_text("AWeber Communications"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
