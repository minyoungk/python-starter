# 혈액형의 개수를 리턴받는 함수
def getCountBlood(blood):
    if blood != 'A' and blood != 'B' and blood != 'AB' and blood != 'O':
        print('입력값이 잘못 되었습니다')
        return False

    bloodList = ['A', 'B', 'AB', 'O', 'O', 'A', 'AB', 'B', 'B', 'AB']

    #카운트 로직실행
    count = 0

    for blood_name in bloodList:
        if blood_name == blood:
            count = count + 1

    return count


blood_input = input()
result = getCountBlood(blood_input)
print(result)