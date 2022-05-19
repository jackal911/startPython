# 별 찍기 - 6 https://www.acmicpc.net/problem/2443
N = int(input())
for i in range(N):
    print(" "*i+"*"*(2*(N-i)-1))
    
'''

# 숏코딩 https://www.acmicpc.net/source/28352970

k=n=int(input())
while n:print(' '*(k-n)+'*'*(2*n-1));n-=1

# 숏코딩에서 for ~ in ~ 절 길이를 줄이려고 k=n=input()과 while n 을 병행해서 쓰는가봄

'''