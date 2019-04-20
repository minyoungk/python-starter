# 과일의 리스트가 있는데
# 과일의 번호입력시 해당과일의 가격을 출력해주고싶어요

aFruitList = ['banana', 'apple', 'pine~~','orange']

name = input()

if aFruitList[0] == name :
    print(3000)
elif aFruitList[1] == name :
    print(2000)
elif aFruitList[2] == name :
    print(2500)
else :
    print('그런 과일 없어요')