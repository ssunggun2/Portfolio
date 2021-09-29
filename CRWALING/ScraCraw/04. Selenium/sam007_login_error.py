##########################
# Selenium
# naver login(error)
# Create by shamantha
##########################

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://naver.net"
driver = webdriver.Chrome(r"D:\ScraCraw\04. Selenium\chromedriver.exe")

try:
    #네이버 이동
    driver.get(url)

    # 로그인 버튼 클릭
    element = driver.find_element_by_class_name("link_login")
    element.click()

    # id, pass 입력(틀린)
    driver.find_element_by_id("id").send_keys("swthinking")
    driver.find_element_by_id("pw").send_keys("ddd")

    
    driver.find_element_by_id("log.login").click()
    driver.find_element_by_id("id").send_keys("swthinking")
    print(driver.page_source)

    # web scraping 작업 시작
except Exception as e:
    print(e)


