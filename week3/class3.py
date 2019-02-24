class common():
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.hp = 100
        self.mp = 100
        self.hp_potion = 10
        self.mp_potion = 10

    def attack(self):
        print("공격 하였습니다")
        self.level_up(50)

    def level_up(self, exp):
        self.exp = self.exp + exp

        if self.exp >= 100 :
            self.exp = 0
            self.level = self.level + 1

char1 = common()
char1.attack()
char1.attack()
print(char1.level)