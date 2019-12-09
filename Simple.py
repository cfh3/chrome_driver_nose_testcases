#!/usr/bin/env python

from selenium import webdriver

EXE_PATH = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=EXE_PATH)
driver.get('https://google.com')
print(driver.page_source)
driver.quit()
