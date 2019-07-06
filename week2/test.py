result = 0 # 최종결과 값 저장 될 변수

# 1~100까지 반복
for i in range(1,101):
    # 짝수인지체크
    if i % 2 == 1:
        result = result + i

print(result)
