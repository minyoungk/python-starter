import requests

r = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=860')
html_soruce = r.text
