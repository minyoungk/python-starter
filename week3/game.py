import random

score = 0 # 골을 넣은 수
count = 0 # 내가 게임을 진행 한 수

while True:
    print("1~6까지 숫자를 입력해주세요")
    user_num = int(input()) # 사용자가 입력한 숫자
    gol_num = random.randrange(1, 7) #골키퍼의 랜덤한 숫자 생성

    if user_num != gol_num: # 나의 입력값과 골키퍼의 랜덤한숫자가 일치한지 체크
        score = score + 1 # 불일치 하는경우는 score를 1 증가

    count = count + 1  # 게임 진행 시 하나씩 증가

    if count > 4:  # count가 5보다 커진경우 결국 -> count 6이 되었을때
        print("점수", score)
        break  # 게임종료
