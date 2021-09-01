import requests
import json
headers = {
     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    #,'sec-fetch-dest': 'document'
    #,'sec-fetch-mode': 'navigate'
    #,'sec-fetch-site': 'none'
    # ,'sec-fetch-user': '?1'
    ,'upgrade-insecure-requests': '1'
    ,'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
response = requests.get("https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=001&aid=001260812", headers=headers)
print(response)
print(response.text)

data = json.loads(response.text)