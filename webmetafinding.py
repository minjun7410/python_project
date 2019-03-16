from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://cs.kookmin.ac.kr/")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject)
#for meta in bsObject.head.find_all('meta'):
#    print(meta.get('content'))