# break And Continue
# break는 아예 탈출
# Continue는 처음 위치로 돌아가서 실행

a = 0
while a < 10 :
    a = a + 1

    if a % 2 == 0 :
        continue

    print(a)