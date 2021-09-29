##########################
# BeautifulSoup
# tag
# Create by shamantha
##########################

import bs4 

html_str = """
<html>
    <body>
        <ul class = "ko">
            <li>
                <a href = "http://www.naver.com/">네이버</a>
            </li>
            <li>
                <a href = "http://www.daum.com/">다음</a>
            </li>
        </ul>
        <ul class = "sns">
            <li>
                <a href = "http://www.google.com/">구글</a>
            </li>
            <li>
                <a href = "http://www.facebook.com/">페이스북</a>
            </li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
atag = bs_obj.find("a")
print(atag['href'])



