##########################
# URLLIB
# Naver Webtoon(태그간 이동)
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
r2 = r1.find_next_sibling("li")  # 이전으로 이동 : find_previous_sibling
print(r2.a.get_text())






