from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager

url = "http://daum.net"
#driver = webdriver.Chrome(r"C:\Users\tmfrl\Desktop\빅데이터\웹크롤링 파일\chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
element = driver.find_element_by_class_name("tf_keyword")

element.send_keys("인기영화")


element = driver.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]") 
                                        
element.click()
