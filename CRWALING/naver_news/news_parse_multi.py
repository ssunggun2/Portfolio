import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=001&aid=0012606140'

def parse_news(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36/87.0.4280.88 Safari/537.36'}
    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.content, 'html.parser')
    title = bs.select_one("div > h3#articleTitle").text
    data = bs.select("span.t11")[0].get_text()
    press = bs.select_one("div.press_logo a img")['title']
    content = bs.select('div#articleBodyContents')[0].get_text().replace('\n','')
    content = content.replace('// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}','')
    content = content.strip()

    print(title)
    print(data)
    print(press)
    print(content)

    return(title, data, press, content, url)


# parse_news(url)

def crawl_news(keyword, ds, de) :
    start = 1
    li = []
    url_format = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}&sort=0&photo=0&field=0&pd=3&ds={}&de={}&cluster_rank=58&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from{}to{},a:all&start={}''https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%A9%94%ED%83%80%EB%B2%84%EC%8A%A4&sort=1&photo=0&field=0&pd=3&ds=2021.08.17&de=2021.08.17&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:from20210817to20210817,a:all&start=381'


    while True : 
        url = url_format.format(keyword, ds, de, ds.replace('.',''), de.replace('.',''), start)

        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36/87.0.4280.88 Safari/537.36'}
        res = requests.get(url, headers=headers)
        bs = BeautifulSoup(res.content, 'html.parser') 

        start_page = int(start/10)+1
        curr_page = int(bs.select('div.sc_page_inner a[aria-pressed="true"]')[0].get_text())

        if start_page > curr_page :
            break
    

        for a_tag in bs.select('div.news_info div.info_group a') :
            if a_tag['href'].startswith('https://news.naver.com') :
                li.append(parse_news(a_tag['href']))
    
        start = start + 10

    df = pd.DataFrame(li, columns=('title', 'media', 'date', 'content', 'url'))
  #df.to_csv("{}_{}_{}.csv".format(keyword, ds.replace('.',''), de.replace('.','')))
    return df

keyword = '메타버스'
ds = '2021.07.17'
de = '2021.07.17'

crawl_news(keyword, ds, de)