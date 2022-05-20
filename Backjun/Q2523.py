# 별 찍기 - 13 https://www.acmicpc.net/problem/2523
N = int(input())
for i in range(-N+1, N):
    print("*"*(N-abs(i)))
    
'''

# 숏코딩 https://www.acmicpc.net/source/5005373

N=int(input())
for i in range(1-N,N):print('*'*(N-abs(i)))

'''