# 소수 구하기 https://www.acmicpc.net/problem/1929
import sys

def primeTF(n:int):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1):
    if primeTF(i) == True:
        sys.stdout.write(str(i)+"\n")

'''시도1 : 소수로 이루어진 집합만 루프를 도는데 왜 더 느릴까?
M, N = map(int, sys.stdin.readline().split())
nums = list(range(M, N+1))
sosus = [2]
output = []
if 2 in nums:
    output.append(str(2))
for i in range(3, N+1):
    sosuTF = True
    for sosu in sosus:
        if sosu>i**0.5:
            break
        if i%sosu==0:
            sosuTF = False
            break
    if sosuTF == True:
        sosus.append(i)
        output.append(str(i)) if i in nums else 0
for j in output:
    sys.stdout.write(j+"\n")
'''