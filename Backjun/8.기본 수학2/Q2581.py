# 소수 https://www.acmicpc.net/problem/2581
from math import ceil, sqrt

M = int(input())
N = int(input())
nums = list(range(M, N+1))
sosu = []
for num in nums:
    if num==1:
        continue
    sosuTF = True
    for i in range(2, ceil(sqrt(num))+1):  # 제곱수의 제곱근까지 포함하기 위한 몸부림
        if num%i==0 and num!=i:
            sosuTF = False
            break
    if sosuTF == True:
        sosu.append(num)
# print(sosu)
if len(sosu):
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)


'''

# 숏코딩 https://www.acmicpc.net/source/25801479

r=range
n,m=map(int,open(0))
print(*[sum(l),l[0]]if(l:=[i for i in r(max(2,n),m+1)if all(i%j for j in r(2,i))])else[-1])

'''