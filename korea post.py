import requests
from bs4 import BeautifulSoup

number = input("택배 운송장 번호를 입력하세요: ")
i = 1
infom = []
temp = ""

request_headers = { 
'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36'), } 

strUrl = "https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm?sid1=" + number
requestSession = requests.Session()
Response = requests.get(strUrl, headers = request_headers)
soup = BeautifulSoup(Response.text, 'html.parser')
while True:
    info = soup.select('#processTable > tbody > tr:nth-child(%d)' % i)
    if not info:
        info = soup.select('#processTable > tbody > tr:nth-child(%d)' % int(i-1))
        for tag in info:
            temp += tag.get_text()
        break
    i = i+1
infom = temp.split('\n')
for _ in range(len(infom)):
    if '\t' in infom[_]: infom[_] = infom[_].replace('\t', '')
if infom[5] == '            ': infom[5] = '배달준비'
print("/// 우체국택배 배송조회 ///\n\n날짜: %s\n시간: %s\n발생국: %s\n처리현황: %s" % (infom[1], infom[2], infom[3], infom[5]))