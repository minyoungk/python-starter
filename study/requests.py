import requests

URL = 'http://13.209.74.170/php-sample/board/list.php'

response = requests.get(URL) # 요청

response.status_code # HTTP 응답코드
# response.text # Response 데이터값

print(response.status_code)
