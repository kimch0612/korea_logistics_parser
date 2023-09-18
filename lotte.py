import requests
import time
from bs4 import BeautifulSoup

number = input("택배 운송장 번호를 입력하세요: ")
i = 1
infom = []
temp = ""

request_headers = { 
'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36'), } 

strUrl = "https://www.lotteglogis.com/mobile/reservation/tracking/linkView?InvNo=" + number
requestSession = requests.Session()
Response = requests.get(strUrl, headers = request_headers)
soup = BeautifulSoup(Response.text, 'html.parser')
info = soup.find("div", "scroll_date_table")
for tag in info:
    temp += tag.get_text()
infom = temp.split('\n')
for _ in range(len(infom)): 
    infom[_] = infom[_].replace('\t', '').replace('\r', '').replace(' ', '').replace(u'\xa0', '')
infom = [v for v in infom if v]
print("/// 롯데택배 배송조회 ///\n\n단계: %s\n시간: %s\n현위치: %s\n처리현황: %s" % (infom[5], infom[6], infom[7], infom[8]))