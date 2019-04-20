# 딕셔너리의 밸류에는 딕셔너리가 또 들어갈수도 있고
# 딕셔너리안에 딕셔너리안에 딕셔너리가 들어갈수도 있다.
# 딕셔너리 밸류안에는 모든 자료형이 들어갈수 있다.

aMemberList = {'짱구' : {'age':7, 'sex':'m'},
               '짱아' : {'age' : 3, 'sex':'f'}}

print(aMemberList['짱구']['age'])

#print(aMemberList[name]['age'])
