##########################
# BeautifulSoup
# Download Image
# 다음영화에서 2019 ~ 2015년까지 상위 5개의 이미지만 다운로드
# Create by shamantha
##########################

import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        print(image["src"])
        img_url = image["src"]
        if img_url.startswith("//"):
            img_url = "https:" + img_url

        print(img_url)
        # 해당사이트에 접속해서 이미지를 가지고 오기위해 다시한번 requests로 접속함
        img_res = requests.get(img_url) 
        img_res.raise_for_status()

        # iamge저장, wb는 이미지가 텍스트가 아니라 바이너리라서 b를 붙여줌
        with open("movie{0}_{1}.jpg".format(idx+1, year), "wb")  as f:
            f.write(img_res.content)

        # 상위 5개의 이미지 다운로드 
        if idx >= 4:
            break;