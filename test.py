#! usr/bin/env python3

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

firefox_path = r'/home/panlijing/Learn/demo/tools/geckodriver'
driver = webdriver.Firefox(executable_path=firefox_path)
driver.get('https://www.baidu.com/')
# driver.get('file:////home/panlijing/Learn/practice/test/none_hidden.html')
# if EC.element_to_be_clickable((By.ID, 'abc')):
#     print('D')
# print(driver.find_element_by_id('yoyo').get_attribute('name'))
# print(driver.find_element_by_id('yy').get_attribute('name'))

# page_source = driver.page_source
# print(page_source)
state = driver.execute_script("return document.readyState")
print(state)
# driver.navigate('http://www.google.com')
driver.quit()
