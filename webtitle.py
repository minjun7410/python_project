from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://cs.kookmin.ac.kr/")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject.head.title)


