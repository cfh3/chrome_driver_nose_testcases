"""
pytest
run all the tests in this file using pytest:
(chrome_driver_tests) ➜  chrome_driver_tests git:(master) ✗ pytest ./ElementTests.py -v -s
specific test only:
(chrome_driver_tests) ➜  chrome_driver_tests git:(master) ✗ pytest ./ElementTests.py::ElementTestsClass::test_dynamic_content -v -s

unittest
run all the tests in this file using unittest:
(chrome_driver_tests) ➜  chrome_driver_tests git:(master) ✗ python -m unittest ElementTests
specific test only:
(chrome_driver_tests) ➜  chrome_driver_tests git:(master) ✗ python -m unittest ElementTests.ElementTestsClass.test_dynamic_content
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
        time.sleep(2)

    def test_floating_menu(self):
        self.driver.get('https://the-internet.herokuapp.com/floating_menu')
        self.assertTrue(self.driver.find_elements_by_css_selector("#menu > ul > li:nth-child(1) > a"), msg="CHIP: couldn't find the button")
        menu_button = self.driver.find_element_by_css_selector("#menu > ul > li:nth-child(1) > a")
        menu_button.click()
        time.sleep(2)
    
    def test_dynamic_content(self):
        self.driver.get('https://the-internet.herokuapp.com/dynamic_content')

        paragraphs_css_selectors = ["#content > div:nth-child(1) > div.large-10.columns",
                                    "#content > div:nth-child(4) > div.large-10.columns",
                                    "#content > div:nth-child(7) > div.large-10.columns"]
        
        for paragraph in paragraphs_css_selectors:
            paragraph_string = self.driver.find_element_by_css_selector(paragraph).text
            word_list = paragraph_string.split()
            specified_length = 12
            word_of_specified_length_exists = False
            word_dict = {}
            
            for word in word_list:
                word_dict[word] = len(word)
            
#            print(word_dict)
            
            # I don't really understand what this does but it works
            longest_word = max(word_dict, key=word_dict.get)
            print(f"\n\nLongest word is: {longest_word}")
            
            for word in word_list:
                if len(word) >= specified_length:
                    print(f"Success!  {word} is {specified_length} chars or greater\n\n")
                    word_of_specified_length_exists = True
                    break
            
            if not word_of_specified_length_exists:
                print(f"Failure!  No word of length {specified_length} chars in the text.\n\n")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
