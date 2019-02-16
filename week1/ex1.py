# 1~100까지 반복하면서 짝수인경우만 값을 다 더해주고싶다

sum = 0;
sum2 = 0;
for i in range(1,101):
    if i % 2 == 0:
        sum = sum + i
    elif i % 2 == 1:
        sum2 = sum2 + i

print(sum)