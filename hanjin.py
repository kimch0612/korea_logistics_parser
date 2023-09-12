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

strUrl = "https://www.hanjin.com/kor/CMS/DeliveryMgr/WaybillResult.do?mCode=MN038&wblnum=" + number + "&schLang=KR"
requestSession = requests.Session()
Response = requests.get(strUrl, headers = request_headers)
soup = BeautifulSoup(Response.text, 'html.parser')
while True:
    info = soup.select('#delivery-wr > div > div.waybill-tbl > table > tbody > tr:nth-child(%d)' % i)
    if not info:
        info = soup.select('#delivery-wr > div > div.waybill-tbl > table > tbody > tr:nth-child(%d)' % int(i-1))
        for tag in info:
            temp += tag.get_text()
        break
    i = i+1
infom = temp.split('\n')
for _ in range(len(infom)):
    if infom[7] == '':
        infom[7] = "(정보 없음)"
print("/// 한진택배 배송조회 ///\n\n날짜: %s\n시간: %s\n상품위치: %s\n배송 진행상황: %s\n전화번호: %s" % (infom[1], infom[2], infom[3], infom[5], infom[7]))