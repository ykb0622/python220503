# web2.py
#웹서버에 페이지 실행 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

# <td class="title">
#                 <a href="/webtoon/detail?">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
#                         </td>

# 페이지 번호 생성
for i in range(1,6):
    url = 
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
    
soup = BeautifulSoup(data, "html.parser")

cartoons = soup.find_all("td", class_="title")
print("개수:{0}".format(len(cartoons)))

# 슬라이싱
# 중단점 추가
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

for tag in cartoons:
    title = tag.find("a")
    print(title.text.strip())
