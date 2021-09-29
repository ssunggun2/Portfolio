##########################
# URLLIB
# errorURL
# Create by shamantha
##########################

from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError

try:
    html = urlopen("http://www.dddsdf.com/kim.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server coult not be found!')
else:
    print("성공")

    
