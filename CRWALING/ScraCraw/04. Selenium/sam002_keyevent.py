##########################
# Selenium
# 클래스로 정보 가지고 오기, Events
# Create by shamantha
##########################

from selenium import webdriver

url = "http://naver.com"
#driver = webdriver.Chrome("D:\\ScraCraw\\04. Selenium\\chromedriver.exe")
#driver = webdriver.Chrome("D:/ScraCraw/04. Selenium/chromedriver.exe")
driver = webdriver.Chrome(r"D:\ScraCraw\04. Selenium\chromedriver.exe")

driver.get(url)
element = driver.find_element_by_class_name("link_login")
print(element)
element.click()

driver.back()
driver.forward()
driver.refresh()
driver.back()



