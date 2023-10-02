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

strUrl = "https://www.ilogen.com/web/personal/trace/" + number
requestSession = requests.Session()
Response = requests.get(strUrl, headers = request_headers)
soup = BeautifulSoup(Response.text, 'html.parser')
while True:
    info = soup.select('body > div.contents.personal.tkSearch > section > div > div.tab_container > div > table.data.tkInfo > tbody > tr:nth-child(%d)' % i)
    if not info:
        info = soup.select('body > div.contents.personal.tkSearch > section > div > div.tab_container > div > table.data.tkInfo > tbody > tr:nth-child(%d)' % int(i-1))
        for tag in info:
            temp += tag.get_text()
        break
    i = i+1
infom = temp.split('\n')
for _ in range(len(infom)): 
    if '\t' in infom[_]: infom[_] = infom[_].replace('\t', '')
infom = [v for v in infom if v]
temp = ''
if "전달" in infom[3]:
    temp = '\n인수자: ' + infom[5]
elif "배달 준비" in infom[3]:
    temp = '\n배달 예정 시간: ' + infom[5]
print("/// 로젠택배 배송조회 ///\n\n날짜: %s\n사업장: %s\n배송상태: %s\n배송내용: %s" % (infom[0], infom[1], infom[2], infom[3]) + temp)