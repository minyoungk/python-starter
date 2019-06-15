class char():
    def __init__(self):
        self.hp = 100 # 속성
        self.mp = 100
        self.str = 4
        self.int = 4

    def attack(self): # 메소드
        print("공격")

    def drinkPotion(self, mode):
        if mode == 'hp':
            self.hp = self.hp+10
        elif mode == 'mp':
            self.mp = self.mp + 10

class sword(char):
    def init(self):
        self.hp = 200
    # 오버라이딩
    # 오버라이딩은 상속받은 메소드를 새로운 프로세스로 덮어씌우는것
    def drinkPotion(self, mode):
        if mode == 'hp':
            self.hp = self.hp+20
        elif mode == 'mp':
            self.mp = self.mp + 10

char1.init()