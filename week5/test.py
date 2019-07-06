from bs4 import BeautifulSoup
import requests

URL = "https://news.nate.com/recent?mid=n0100"
res = requests.get(URL)

print(res.text)