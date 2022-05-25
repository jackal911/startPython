# 팩토리얼 https://www.acmicpc.net/problem/10872
def facto(N: int):
    if N>1:
        return N*facto(N-1)
    else:
        return 1
print(facto(int(input())))

'''

# 숏코딩 https://www.acmicpc.net/source/1103413

import math
print(math.factorial(int(input())))

# math 모듈에 팩토리얼이 있다.

'''