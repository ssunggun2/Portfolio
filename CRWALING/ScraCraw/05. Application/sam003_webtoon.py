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
r2 = r1.next_sibling.next_sibling
print(r2.a.text)
r3 = r2.next_sibling.next_sibling
print(r3.a.text)

pr2 = r3.previous_sibling.previous_sibling
print(pr2.a.text)

print(r1.parent)


