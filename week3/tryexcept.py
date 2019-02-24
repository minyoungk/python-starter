#예외처리
#예외를 처리하기 위한것
#try except문

try:
    number = int(input())
except IndexError:
    print("숫자만 입력해라")
except SyntaxError:
    print("숫자만 입력해라")