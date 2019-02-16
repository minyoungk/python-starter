# 리스트에 혈액형이 있는데
# 각 혈앵형별 개수가 궁금해요

bloodList = ['A','B','AB','O','O','A','AB','B','B','AB','P']

#변수가 최소 4개는 나와야해요

acount = 0
abcount = 0
ocount = 0
bcount = 0

for blood in bloodList:
    if blood == 'A' :
        acount = acount + 1
    elif blood == 'B' :
        bcount = bcount + 1
    elif blood == 'AB':
        abcount = abcount + 1
    elif blood == 'O':
        ocount = ocount + 1
    else:
        print("형태가 맞지 않는 값이 포함되어있어요. 확인하세요")