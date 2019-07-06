from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql

con=pymysql.connect(host = '15.164.95.84', user = 'root', password = 'qwer1234', db = 'study')
curs = con.cursor()

# -> insert하는 방법, 나만의 테이블(정보를 담을 테이블)
Song_name=[]
Song_singer=[]
driver = webdriver.Chrome('./chromedriver')
URL = 'https://www.melon.com/chart/day/index.htm?classCd=DM0000'
driver.get(URL)
soup = BeautifulSoup(driver.page_source,'html.parser')

for SongInfo in soup.find_all("a", class_="image_typeAll"):
    print(SongInfo.img.get('src'))

for SongInfo in soup.find_all("div", class_="ellipsis rank01"):
   Song_name.append(SongInfo.find_all("a")[0].text)
for SongInfo in soup.find_all("div", class_="ellipsis rank02"):
   Song_singer.append(SongInfo.find_all("a")[0].text)

driver.close()

# INSERT
sql = 'INSERT INTO melon (song, singer) VALUES (%s, %s)'

for i in range(0,100):
    curs.execute(sql, (Song_name[i], Song_singer[i]))

con.commit()