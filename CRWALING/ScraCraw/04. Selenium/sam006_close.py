##########################
# Selenium
# close
# Create by shamantha
##########################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://daum.net"
driver = webdriver.Chrome(r"D:\ScraCraw\04. Selenium\chromedriver.exe")

driver.get(url)

#driver.close()   # 현재 탭만 종료
driver.quit()    # 브라우저 자체를 종료

