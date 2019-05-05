class basic():
    def __init__(self):
        self.level = 1
        self.str = 5
        self.int = 5
        self.luk = 5
        self.dex = 5
        self.st_point = 0
        self.exp = 0

    def attack(self):
        print("공격!")
        self.exp = self.exp + 50
        self.levelup()

    def levelup(self):
        if self.exp >= 100:
            print("레벨업!!")
            self.st_point = self.st_point + 3
            self.level = self.level + 1
            self.exp = 0

    def str_up(self):
        if self.st_point < 1:
            print("남은 스텟포인트가 존재 하지 않습니다.")
            return False

        self.str = self.str + 1
        self.st_point = self.st_point - 1

class magician(basic):
    def attack(self):
        print("공격!")
        self.exp = self.exp + 20
        self.levelup()

char1 = magician()
print(char1.exp)
char1.attack()
print(char1.exp)