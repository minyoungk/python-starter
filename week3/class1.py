# class 정의시 class 클래스명
# __init__ 은 클래스 최초생성시 제일먼저 실행 된다
# init에서는 속성값에 대한 초기화, 특정메서드 실행등의 행위가 들어간다
#
# self는 클래스를 호출한 그놈 그 자체
# 클래스 생성시 값을 넘겨줄수 있다
# __init__에서 매개변수로 받는데 첫번째 self가아닌 두번째부터 매칭된다.

class char():
    def __init__(self):
        self.hp = 100
        self.mp = 100
        self.str = 4
        self.int = 4
        self.dex = 4

    def attack(self):
        print("공격!!!")
        self.mp = self.mp - 3

    def drink_potion(self, type):
        if type == 'hp':
            self.hp = self.hp + 10
        elif type == 'mp':
            self.mp = self.mp + 10


# 상속
class magician(char):
    # 오버라이딩
    def drink_potion(self, type):
        if type == 'hp':
            self.hp = self.hp + 50
        elif type == 'mp':
            self.mp = self.mp + 50


char1 = magician()
char1.drink_potion('hp')
print(char1.hp)






#
# class magician:
#     def __init__(self, item = '', i):
#         # 속성값
#         self.hp = 100
#         self.mp = 200
#         self.str = 5
#         self.item = item
#
#     def attack(self):
#         print('공격')
#         self.mp = self.mp - 10
#
# char1 = magician('item', 3) #클래스를 생성
# char1.attack()
# print(char1.mp)