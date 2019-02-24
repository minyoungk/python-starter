# class 정의시 class 클래스명
# __init__ 은 클래스 최초생성시 제일먼저 실행 된다
# init에서는 속성값에 대한 초기화, 특정메서드 실행등의 행위가 들어간다
# self는 클래스를 호출한 그놈 그 자체
# 클래스 생성시 값을 넘겨줄수 있다
# __init__에서 매개변수로 받는데 첫번째 self가아닌 두번째부터 매칭된다.

class magician:
    def __init__(self, item, mode):
        # 속성값
        self.max_hp = 150
        self.hp = 100
        self.mp = 200
        self.str = 5

        print(item)

char1 = magician('Item') #클래스를 생성

char1.attack() #클래스에 메소드(함수)를 사용
char1.drink_potion()
char1.drink_potion()

print(char1.hp) #클래스에 속성값에 접근