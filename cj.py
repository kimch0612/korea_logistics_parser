import requests
from bs4 import BeautifulSoup

number = input("택배 운송장 번호를 입력하세요: ")
i = 1

request_headers = { 
'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36'), } 

strUrl = "https://trace.cjlogistics.com/tracking/jsp/cmn/Tracking_new.jsp?QueryType=3&pTdNo=" + str(number)
requestSession = requests.Session()
Response = requests.get(strUrl, headers = request_headers)
soup = BeautifulSoup(Response.text, 'html.parser')

while True:
    info = soup.select('#content > div > table.tepTb02.tepDep02 > tbody > tr:nth-child(%d)' % i)
    if not info:
        info = soup.select('#content > div > table.tepTb02.tepDep02 > tbody > tr:nth-child(%d)' % int(i-1))
        for tag in info:
            print(tag.get_text())
        break
    i = i+1