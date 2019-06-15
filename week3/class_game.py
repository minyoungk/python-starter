# 빙고
import random

bingo = []
bingo_check = []

# 빙고 체크를 위한 리스트에 값 넣어주기
for i in range(0,25):
    bingo_check.append(0)

# 빙고판 만들기
while len(bingo) < 25:
    num = random.randrange(1, 26)

    if len(bingo) != 0:
        if num in bingo:
            continue

    bingo.append(num)


def checkBingo(bingo_check):
    count = 0

    # 첫번째행 체크
    if bingo_check[0] == 1 and bingo_check[1] == 1 and bingo_check[2] == 1 and bingo_check[3] == 1 and bingo_check[4] == 1:
        count = count + 1

    # 두번째행체크
    if bingo_check[5] == 1 and bingo_check[6] == 1 and bingo_check[7] == 1 and bingo_check[8] == 1 and bingo_check[9] == 1:
        count = count + 1

    # 세번째행체크
    if bingo_check[10] == 1 and bingo_check[11] == 1 and bingo_check[12] == 1 and bingo_check[13] == 1 and bingo_check[14] == 1:
        count = count + 1

    # 네번째행체크
    if bingo_check[15] == 1 and bingo_check[16] == 1 and bingo_check[17] == 1 and bingo_check[18] == 1 and bingo_check[19] == 1:
        count = count + 1

    # 다섯번째행체크
    if bingo_check[20] == 1 and bingo_check[21] == 1 and bingo_check[22] == 1 and bingo_check[23] == 1 and bingo_check[24] == 1:
        count = count + 1

    # 첫열체크
    if bingo_check[0] == 1 and bingo_check[5] == 1 and bingo_check[10] == 1 and bingo_check[15] == 1 and bingo_check[20] == 1:
        count = count + 1

    # 둘째열체크
    if bingo_check[1] == 1 and bingo_check[6] == 1 and bingo_check[11] == 1 and bingo_check[16] == 1 and bingo_check[21] == 1:
        count = count + 1

    # 셋째열체크
    if bingo_check[2] == 1 and bingo_check[7] == 1 and bingo_check[12] == 1 and bingo_check[17] == 1 and bingo_check[22] == 1:
        count = count + 1

    # 넷째열체크
    if bingo_check[3] == 1 and bingo_check[8] == 1 and bingo_check[13] == 1 and bingo_check[18] == 1 and bingo_check[23] == 1:
        count = count + 1

    # 다섯째열체크
    if bingo_check[4] == 1 and bingo_check[9] == 1 and bingo_check[14] == 1 and bingo_check[19] == 1 and bingo_check[24] == 1:
        count = count + 1

    # 첫번째 대각선
    if bingo_check[0] == 1 and bingo_check[6] == 1 and bingo_check[12] == 1 and bingo_check[18] == 1 and bingo_check[24] == 1:
        count = count + 1

    # 두번째 대각선
    if bingo_check[4] == 1 and bingo_check[8] == 1 and bingo_check[12] == 1 and bingo_check[16] == 1 and bingo_check[20] == 1:
        count = count + 1

    return count

# 빙고게임 진행
while True:
    try:
        num = int(input())
    except:
        print("다시 입력 하세요")
        continue

    if num > 25:
        print("25보다 큰 값은 입력 불가")
        continue

    index = bingo.index(num)
    if bingo_check[index] == 1:
        print("이미 외친 값")
        continue

    bingo_check[index] = 1

    bingo_count = checkBingo(bingo_check);

    if bingo_count > 4:
        print("빙고!")
        break

    print(bingo[0:5])
    print(bingo[5:10])
    print(bingo[10:15])
    print(bingo[15:20])
    print(bingo[20:25])
    print("\n")
    print(bingo_check[0:5])
    print(bingo_check[5:10])
    print(bingo_check[10:15])
    print(bingo_check[15:20])
    print(bingo_check[20:25])

