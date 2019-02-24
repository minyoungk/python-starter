class common():
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.hp = 100
        self.mp = 100
        self.hp_potion = 10
        self.mp_potion = 10

        self.init()

    def init(self):
        print("재정의")

    def attack(self):
        print("공격 하였습니다")
        self.level_up(50)

    def level_up(self, exp):
        self.exp = self.exp + exp

        if self.exp >= 100 :
            self.exp = 0
            self.level = self.level + 1

    def drink_potion(self, mode):
        if mode == 'hp' :
            self.hp_potion = self.hp_potion - 1
            self.hp = self.hp + 30
        elif mode == 'mp' :
            self.mp_potion = self.mp_potion - 1
            self.mp = self.mp + 30

class magician(common):
    def init(self):
        self.skill_level = 1

    def do_skill(self):
        damage = self.skill_level * 10
        self.skill_level = self.skill_level + 1
        self.mp = self.mp - 30

        print('스킬!!')

        return damage

    def drink_potion(self, mode = 'hp'):
        if mode == 'hp' :
            print(self.hp_potion)
        elif mode == 'mp' :
            self.mp_potion = self.mp_potion - 1
            self.mp = self.mp + 50

char1 = magician()
char1.do_skill()
char1.drink_potion()
print(char1.hp)
print(char1.mp)



