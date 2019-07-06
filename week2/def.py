def sum(list):
    # 최종결과값을 담을 변수(박스)
    result = 0

    # 리스트 반복(최종결과값 변수에 값을 넣어준다)
    for i in list:
        result = result + i

    # 최종결과값 리턴
    return result

numberList = [3,4,5,2,4,4]
a = sum(numberList)

print(a)