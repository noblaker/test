
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://baidu.com')

driver.find_element_by_id('kw').send_keys('Selenium2')
driver.find_element_by_id('su').click()
time.sleep(2)
driver.quit()
