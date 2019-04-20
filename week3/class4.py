import random

class taja():
    def __init__(self):
        self.score = 0
        self.str = 1

    def homerun(self):
        self.score = self.score + ( 30 * self.str )

class tusu():
    def __init__(self):
        self.score = 0
        self.str = 1

    def strike(self):
        self.score = self.score + 5

ball_count = 0
taja1 = taja()
tusu1 = tusu()

while True:
    try:
        number = int(input())
    except:
        print("숫자만 입력해!")
        continue

    tusu_number = random.randrange(1,10)

    if number == tusu_number:
        print("홈런")
        taja1.homerun()
    elif tusu_number == 1 or tusu_number == 3:
        print("볼")
        ball_count = ball_count + 1
        if ball_count > 4:
            taja1.score = taja1.score + 10
    else:
        print("스트라이크")
        tusu1.strike()

    if taja1.score >= 60:
        print("타자가 승리 했습니다")
        break

    if tusu1.score >= 60:
        print("투수가 승리 했습니다")
        break