import requests # HTML을 받아오기 위한 목적
from bs4 import BeautifulSoup # HTML소스에서 내가 원하는값을 빼오기위한 목적

URL = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1"
res = requests.get(URL) # HTML을 받아오는 로직

bsObject = BeautifulSoup(res.text, "html.parser")
nums = bsObject.find("div", class_="num win")

for span in nums.find_all("span"):
    print(span.text)