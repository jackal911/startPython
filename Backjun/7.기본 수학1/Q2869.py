# 달팽이는 올라가고 싶다 https://www.acmicpc.net/problem/2869
import math
A, B, V = map(int, input().split())
print(math.ceil((V-A)/(A-B))+1)

'''

# 숏코딩 https://www.acmicpc.net/source/5154286

a,b,v=map(int,input().split());print(1-(a-v)//(a-b))

# 음수를 나눈 몫은 절대값이 큰 값으로 산출된다는 걸 이용해서 ceil대신에 사용했다. 신선한 방식.

'''

'''시도1
A, B, V = map(int, input().split())
curD = A
i = 1
while True:
    # print(curD)
    if curD >= V:
        print(i)
        break
    curD += (A - B)
    i += 1
'''
