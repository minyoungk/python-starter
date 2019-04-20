# 상속
# 공통적인 기능을 빼서 상속을 받을 수 있다.
# 상속을 받을때는 class 클래스명(상속받은 클래스명)
# 오버라이딩
# - 상속받은 메소드를 새로운 메소드로직으로 덮어쓴다.

class common:
    def __init__(self):
        self.m = 0 #미네랄
        self.g = 0 #가스

    def getM(self): #미네랄 캐는 메소드
        self.m = self.m + 4

    def getG(self): #가스 캐는 메소드
        self.g = self.g + 3

class prot(common): #프로토스 종족
    def getM(self): #미네랄 캐는 메소드
        self.m = self.m + 6

    def makeProve(self):
        if self.m < 3:
            print('미네랄이 부족합니다')
        elif self.g < 1:
            print('가스가 부족합니다')
        else: # 프로브를 뽑기위해서 미네랄이 3, 가스가1이 필요합니다
            self.m = self.m - 3
            self.g = self.g - 1

            print('프로브 생성 완료')

prot1 = prot()
prot1.getM()
prot1.getG()

prot1.makeProve()
prot1.makeProve()
prot1.makeProve()
prot1.makeProve()

# class zerg(common):
#     def makeDron(self):
#         if self.m < 4 or self.g < 2:
#             print('가스와 미네랄이 부족합니다')
#         else:
#             self.m = self.m - 3
#             self.g = self.g - 1
#
#             print('프로브 생성 완료')
#
# prot1 = prot()
# zerg1 = zerg()
#
# prot1.getM()
# print(prot1.m)
