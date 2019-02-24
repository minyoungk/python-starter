# 학생의 나이를 알려주는 함수
def getAgeInMember(member, name):
    return member[name]['age']

member = {
    '짱구' : { 'age' : 7, 'sex' : 'M'},
    '짱아' : { 'age' : 4, 'sex' : 'F'},
    '맹구' : { 'age' : 8, 'sex' : 'M'}
}

name = input()
result = getAgeInMember(member, name)
print(result)
