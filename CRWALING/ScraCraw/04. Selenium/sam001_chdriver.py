##########################
# Selenium
# Execute chrome driver
# Create by shamantha
##########################

from selenium import webdriver

url = "http://naver.com"
#driver = webdriver.Chrome("D:\\ScraCraw\\04. Selenium\\chromedriver.exe")
#driver = webdriver.Chrome("D:/ScraCraw/04. Selenium/chromedriver.exe")
#driver = webdriver.Chrome(r"D:\ScraCraw\04. Selenium\chromedriver.exe")
driver = webdriver.Chrome(r"chromedriver.exe")


driver.get(url)



