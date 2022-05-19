# 별 찍기 - 7 https://www.acmicpc.net/problem/2444
N = int(input())
i = 0
while i<N:
    print(" "*(N-i-1)+"*"*(2*i+1))
    i += 1

i -= 1

while i:
    i -= 1
    print(" "*(N-i-1)+"*"*(2*i+1))
    
'''

# 숏코딩 https://www.acmicpc.net/source/22352624

n=int(input())
for i in range(-n+1,n):i=abs(i);print(' '*i+'*'*((n-i)*2-1))

# 별 개수가 늘어났다가 줄어드는 것을 절대값을 이용해서 한번에 표현함

'''