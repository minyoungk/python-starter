# 파일을 생성하거나 열때는 open 이라는 함수를 이용한다
# open함수의 첫번째 매개변수값은 파일의이름 두번째 매개변수값은 모드
# 모드 w = 쓰기모드 , a = 추가모드, r = 읽기모드
# 파일이 존재하지 않으면 파일을 새로 생성하고
# 파일이 존재하면 파일을 덮어씌운다(w모드) 파일에 내용을 추가한다(a모드)
# 변수명.write 파일에 내용쓰기

f = open("새파일.txt", 'a', encoding='utf8')

for i in range(1, 11):
    data = "1.1.1.1 hanabank.com"
    f.write(data)

f.close()