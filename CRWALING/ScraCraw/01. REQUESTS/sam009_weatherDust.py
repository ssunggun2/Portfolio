##########################
# REQUSTS
# 네이버 날씨 미세먼지 가져오기
# Create by shamantha
##########################

# 웹 페이지 가져오기
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
pprint(html.text)

# 파싱
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

soup = bs(html.text,'html.parser')

# 요소 1개 찾기
from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text,'html.parser')

data1 = soup.find('div',{'class':'detail_box'})
pprint(data1)

# 요소 모두 찾기(findAll)
from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text,'html.parser')

data1 = soup.find('div',{'class':'detail_box'})
#pprint(data1)

data2 = data1.findAll('dd')
pprint(data2)

# 내부 텍스트 추출
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text,'html.parser')

data1 = soup.find('div',{'class':'detail_box'})
#pprint(data1)

data2 = data1.findAll('dd')
# pprint(data2)

fine_dust = data2[0].find('span',{'class':'num'})
print(fine_dust)

#--------------
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text,'html.parser')

data1 = soup.find('div',{'class':'detail_box'})
#pprint(data1)

data2 = data1.findAll('dd')
# pprint(data2)

fine_dust = data2[0].find('span',{'class':'num'}).text
print(fine_dust)

# 초미세먼지 추출
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text,'html.parser')

data1 = soup.find('div',{'class':'detail_box'})
#pprint(data1)

data2 = data1.findAll('dd')
# pprint(data2)

fine_dust = data2[0].find('span',{'class':'num'}).text
print(fine_dust)

ultra_fine_dust = data2[1].find('span',{'class':'num'}).text
print(ultra_fine_dust)