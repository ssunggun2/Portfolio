# -*- coding: utf-8 -*-
"""
한국기업 지배 구조
"""

import requests
import csv
from bs4 import BeautifulSoup
url = "http://www.cgs.or.kr/business/esg_tab04.jsp?pg=1&pp=10&skey=&svalue=&sfyear=2020&styear=2020&sgtype=TOTAL&sgrade=A%EF%BC%8B#ui_contents"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text ,"html.parser")
table = soup.find("div", {"class", "business_board"})

print(table)
data = []
for row in table.findAll("tr"):
    cols = row.findAll("td")
    
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    print(cols)
# print(data)
    
    # td = data.findAll('td')
# esg_apluss  = soup.findAll("tr")

# print()
# # tmp = [[],[],[],[],[],[],[],[],[]]
# tmp1 = []
# for idx, esg_aplus in enumerate(esg_apluss):
#     type(esg_aplus.text)
#     # tmp1[idx]= esg_aplus.text
#     # print(idx)
#     # tmp[idx] = esg_aplus.text
#     if idx == 10:
#         break
# print(tmp1)
# # print(tmp)
# # print(tmp1)
# # with open("esg.csv", "w",newline="" ) as f:
# #     wr = csv.writer(f)
# #     wr.writerows(tmp1)
