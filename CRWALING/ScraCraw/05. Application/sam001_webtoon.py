##########################
# URLLIB
# Naver Webtoon(페이지 정보를 잘 모를경우)
# Create by shamantha
##########################

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# # 페이지에 대한 정보를 잘 모를때
print(soup.find("a", attrs = {"class":"Nbtn_upload"}))
print(soup.find(attrs = {"class":"Nbtn_upload"}))       #class가 유니크 할 경우 element 생략 가능, 위와 동일

