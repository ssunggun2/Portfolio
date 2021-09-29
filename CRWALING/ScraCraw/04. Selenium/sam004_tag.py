##########################
# Selenium
# TAG로 정보 가지고 오기
# Create by shamantha
##########################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "http://naver.com"
driver = webdriver.Chrome(r"chromedriver.exe")

driver.get(url)
element = driver.find_element_by_tag_name("a")
elements = driver.find_elements_by_tag_name("a")

for idx, e in enumerate(elements):
    ele = e.get_attribute('href')
    print(ele)
    time.sleep(0.5)

    