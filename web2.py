# web2.py
#웹서버에 페이지 실행 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

# <td class="title">
#                 <a href="/webtoon/detail?">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
#                         </td>


data = urllib.request.urlopen(
    "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

soup = BeautifulSoup(data, "html.parser")

cartoons = soup.find_all("td", class_="title")
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)
