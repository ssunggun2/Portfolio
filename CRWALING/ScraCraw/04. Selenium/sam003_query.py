##########################
# Selenium
# Query
# Create by shamantha
##########################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://naver.com"
driver = webdriver.Chrome(r"D:\ScraCraw\04. Selenium\chromedriver.exe")

driver.get(url)
element = driver.find_element_by_id("query")
element.send_keys("컴퓨터")
element.send_keys(Keys.ENTER)

'''
driver.get(url)
element = driver.find_element_by_id("query")
element.send_keys("컴퓨터")
element.send_keys(Keys.ENTER)

element = driver.find_element_by_id("nx_query")
element.clear()
'''

