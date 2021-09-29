##########################
# REQUSTS
# 데이터(HTML) 가지고 오기
# Create by shamantha
##########################

import requests

res = requests.get("http://naver.com")
#res = requests.get("http://yyy.tistory.com")

res.raise_for_status()
print("정상입니다.")
print(len(res.text))
print(res.text)




