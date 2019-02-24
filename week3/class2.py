# 상속
# 공통적인 기능을 빼서 상속을 받을 수 있다.
# 상속을 받을때는 class 클래스명(상속받은 클래스명)
# 오버라이딩
# - 상속받은 메소드를 새로운 메소드로직으로 덮어쓴다.

class common:
    def __init__(self):
        self.m = 0
        self.g = 0

    def getM(self):
        self.m = self.m + 4

    def getG(self):
        self.g = self.g + 3

class prot(common):
    def getM(self):
        self.m = self.m + 5

    def makeProve(self):
        if self.m < 4 or self.g < 2:
            print('가스와 미네랄이 부족합니다')
        else:
            self.m = self.m - 3
            self.g = self.g - 1

            print('프로브 생성 완료')

class zerg(common):
    def makeDron(self):
        if self.m < 4 or self.g < 2:
            print('가스와 미네랄이 부족합니다')
        else:
            self.m = self.m - 3
            self.g = self.g - 1

            print('프로브 생성 완료')

prot1 = prot()
zerg1 = zerg()

prot1.getM()
print(prot1.m)