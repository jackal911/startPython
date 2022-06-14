# 부녀회장이 될테야 https://www.acmicpc.net/problem/2775
from copy import deepcopy

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    lower_floor = list(range(1, n+1))  # 0층으로 초기화
    resident = list(range(n))
    for i in range(1, k+1):        
        for j in range(n):
            resident[j] = sum(lower_floor[:j+1])
        lower_floor = deepcopy(resident)  # 단순히 = 으로 처리하면 두 list가 같은 변수 주소를 공유한다.
    print(resident[n-1])

'''

# 숏코딩 https://www.acmicpc.net/source/29730930

import math
i=input
for n in[int]*int(i()):k=n(i());print(math.comb(k+n(i()),k+1))

'''