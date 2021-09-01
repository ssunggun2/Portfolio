# import requests
# import json

# ##어디서 불러오는 거였더라??

# params = {'suppress_response_codes' : True
#         ,'callback' : 'jQuery11240692148809744773_1629262052150'
#         , 'q' : 'NEWS%5Bne_417_0000726114%5D%7CNEWS_SUMMARY%5B417_0000726114%5D%7CJOURNALIST%5B76236(period)%5D%7CNEWS_MAIN%5Bne_417_0000726114%5D'
#         , 'isDuplication' : False
#         , '_' : '1629262052151'
# }

# response = requests.get('https://news.like.naver.com/v1/search/contents',
#                          params = params)

# print(response)
# print(response.text)

import requests
import json

##어디서 불러오는 거였더라??

oid = '001'
aid = '0012604850'
params = {
    'suppress_response_codes': True
    #,'callback': 'jQuery1124005705702844427485_1629261815444'
    ,'q': f'''NEWS[ne_{oid}_{aid}]|NEWS_SUMMARY[{oid}_{aid}]|JOURNALIST[76236(period)]|NEWS_MAIN[ne_{oid}_{aid}]'''
    ,'isDuplication': False
    ,'_':1629261815445
}
response = requests.get('https://news.like.naver.com/v1/search/contents',
                        params=params)


data = json.loads(response.text)
result = []
for d in data['contents'][0]['reactions']:
    result.append({
        d['reactionType']:d['count']
    })
print(result)


