# import 모듈명
# 모듈명은 "경로"를 입력해주고 .py는 제외

import calc

result = calc.add(3,4)

print(result)











# from 모듈명 import 함수명, 함수명2 ....
from calc import add, sub

result = add(3,5)
print(result)
