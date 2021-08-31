import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=001&aid=0012606140'

def parse_news(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36/87.0.4280.88 Safari/537.36'}
    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.content, 'html.parser')
    title = bs.select_one("div > h3#articleTitle").text
    data = bs.select("span.t11")[1].get_text()
    press = bs.select_one("div.press_logo a img")['title']
    content = bs.select('div#articleBodyContents')[0].get_text().replace('\n','')
    content = content.replace('// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}','')
    content = content.strip()

    print(title)
    print(data)
    print(press)
    print(content)

    return(title, data, press, content)


parse_news(url)