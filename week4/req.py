import requests # HTML소스를 받기 위한 모듈
from bs4 import BeautifulSoup # HTML소스 내용에 접근하기 위한 모듈

bigBox = {} # 큰박스

for i in range(1,6):
    # HTML소스를 받기 위한 요청
    r = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='+str(i))

    # HTML소스 받은 내용을 BS 넘긴다
    soup = BeautifulSoup(r.text, 'html.parser')

    # BS에서 HTML 접근
    divtag = soup.find("div", class_="num win")

    smallBox = [] #작은박스 각 회차별 정보가 들어가는 용도

    for span in divtag.find_all('span'):
        smallBox.append(span.text)

    bigBox[i] = smallBox

print(bigBox)
