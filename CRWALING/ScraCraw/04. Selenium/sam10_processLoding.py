##########################
# Selenium
# 네이버 항공권(delay 처리 : error)
# Create by shamantha
##########################


from selenium import webdriver

#################################################################
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#################################################################

driver = webdriver.Chrome(r"D:\ScraCraw\04. Selenium\chromedriver.exe")
driver.maximize_window()

url = "https://flight.naver.com/flights/"
driver.get(url)

try:
    driver.find_element_by_link_text("가는날 선택").click()

    # 가는날 선택(이번달)
    driver.find_elements_by_link_text("29")[0].click()
    driver.find_elements_by_link_text("30")[0].click()

    # 여행지 선택
    driver.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/dl").click() 

    # 항공권 검색 클릭
    driver.find_element_by_link_text("항공권 검색").click()

    # EC.presence_of_element_located : 어떠한 element가 나올때까지 기다려 달라라는 의미
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(element.text)
except Exception as e:
    print(e)
finally:
    print("success")
    driver.quit()