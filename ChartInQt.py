import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.inven.co.kr/board/autochess/5416?category=%EC%A0%95%EB%B3%B4')
html = req.text
pars = BeautifulSoup(html, 'html.parser')
notice_list = pars.select(
    "td.bbsSubject > a"
)
print(notice_list)
for i in range(5):
    print(notice_list[i].get_text())
#powerbbsBody > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > form > table > tbody >
#powerbbsBody > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > form > table > tbody > tr:nth-child(7) > td.bbsSubject > a