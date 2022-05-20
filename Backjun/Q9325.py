# 얼마? https://www.acmicpc.net/problem/9325
N = int(input())
for _ in range(N):
    sum = 0
    s = int(input())
    sum += s
    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        sum += q*p
    print(sum)
    
'''

# 숏코딩 https://www.acmicpc.net/source/435212

r=lambda:int(input())
for _ in range(r()):
    s=r()
    for i in range(r()):b,c=map(int,input().split());s+=b*c
    print(s)

# lambda를 이용해서 int(input())를 r에 담을 수 있다는걸 처음 배웠다

'''