# web1.py
from bs4 import BeautifulStoneSoup

# 페이지로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체
soup = BeautifulStoneSoup(page, "html.parser")
print(soup.prettify())

