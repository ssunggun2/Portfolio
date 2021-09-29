##########################
# URLLIB
# errorHttp
# Create by shamantha
##########################

from urllib.request import urlopen
from urllib.request import HTTPError

try:
    html = urlopen("http://www.google.com/kim.html")
except HTTPError as e:
    print(e)
else:
    print("성공")





