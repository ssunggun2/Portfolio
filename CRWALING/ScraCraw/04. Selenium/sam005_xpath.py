##########################
# Selenium
# XPATH
# Create by shamantha
##########################
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://daum.net"
driver = webdriver.Chrome(r"D:\ScraCraw\04. Selenium\chromedriver.exe")

driver.get(url)
element = driver.find_element_by_class_name("tf_keyword")
element.send_keys("인기영화")

# element = driver.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
element = driver.find_element_by_css_selector("#daumSearch > fieldset > div > div > button.ico_pctop.btn_search") 
element.click()
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

url = "http://daum.net"
driver = webdriver.Chrome(r"chromedriver.exe")

driver.get(url)
element = driver.find_element_by_class_name("link_login")
element.send_keys("인기영화")


element = driver.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]") 

                                        
element.click()
