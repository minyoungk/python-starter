from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

URL = 'https://land.naver.com/article/divisionInfo.nhn?cortarNo=1117000000&rletNo=&rletTypeCd=A01&tradeTypeCd=&hscpTypeCd=A01%3AA03%3AA04&cpId=&location=&siteOrderCode='

driver.get(URL)
bsObject = BeautifulSoup(driver.page_source, "html.parser")

bsObject2 = bsObject.find('table', class_='sale_list _tb_site_img NE=a:cpm')

#거래 가져오기
for a in bsObject2.find_all('div', class_='inner pl4'):
    print(a.text)

#종류 가져오기

#확인일자 가져오기

