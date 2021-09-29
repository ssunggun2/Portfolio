##########################
# REQUSTS
# 연결 에러 처리
# Create by shamantha
##########################

import requests

# res = requests.get("http://naver.com")
res = requests.get("http://yyy.tistory.com")

if res.status_code == requests.codes.ok:
    print("정상")
else:
    print("오류 : ", res.status_code)

    



