from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://cs.kookmin.ac.kr/")#python insterpreter
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject)