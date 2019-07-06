import requests
from bs4 import BeautifulSoup
import  pymysql
conn = pymysql.connect(host = '54.180.121.145', user = 'root',password = 'qwer1234',db = 'study')
curs = conn.cursor()

URL = "https://movie.naver.com/movie/running/current.nhn"

res=requests.get(URL)
soup = BeautifulSoup(res.text,'html.parser')

Movie = {}
count =0

ultag = soup.find("ul",class_="lst_detail_t1")

key_count = 1
for name in ultag.find_all("dt", class_="tit"):
    #print(name.a.text)
    Movie[key_count]={} #무비박스 안을 딕셔너리로 정의해줌
    Movie[key_count]["name"]=name.a.text
    key_count = key_count + 1

key_count = 1 #다음 for문을 위해 key_count를 리셋해줌
for image in ultag.find_all("img"):
    #print(image.get('src'))
    Movie[key_count]["image"]=image.get('src')
    key_count = key_count +1

key_count = 1
for dltag in ultag.find_all("dl", class_="info_star"):
    score = dltag.find("span", class_="num")
    Movie[key_count]["score"] = score.text
    key_count = key_count + 1

for key, value in Movie.items():
    print(key)
    print(value)

    # SQL문 작성
    sql = 'INSERT INTO naverMovie (name, image, score) VALUES (%s, %s, %s)'

    curs.execute(sql, (value['name'], value['image'], value['score']))
    conn.commit()


