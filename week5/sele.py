import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

lottoDic = {} #로또 최종값을 저장하기 위한 변수

# i는 URL조회시 GET의 파라미터값으로 사용하기 위해 사용
for i in range(845,851):

    URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='+str(i)

    driver.get(URL)
    bsObject = BeautifulSoup(driver.page_source, "html.parser")

    nums = bsObject.find("div", class_="num win")

    lottoNums = []
    for atag in nums.find_all('a'):
        lottoNums.append(atag.string)

    lottoDic[i] = lottoNums

print(lottoDic)
