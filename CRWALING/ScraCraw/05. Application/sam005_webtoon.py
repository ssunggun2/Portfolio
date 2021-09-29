##########################
# URLLIB
# Naver Webtoon(태그정보 리스팅)
# Create by shamantha
##########################

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# 태그간 이동
r1 = soup.find("li", attrs = {"class":"rank01"})
print(r1.a.get_text())
r2 = r1.find_next_siblings("li") # 모든 형제들 가지고 옴

print(r2)






