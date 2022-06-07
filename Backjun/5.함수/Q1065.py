# 한수 https://www.acmicpc.net/problem/1065
def hansu(n:int):
    if n//100==0:
        return 1
    difference = int(str(n)[1])-int(str(n)[0])
    for i in range(2, len(str(n))):
        if int(str(n)[i])-int(str(n)[i-1])!=difference:
            return 0
    return 1

N = int(input())
print(sum(hansu(n) for n in range(1, N+1)))
