# 벌집 https://www.acmicpc.net/problem/2292
def beeHouse(N:int):
    if N==1:
        return 1
    i = 0
    while True:
        i += 1
        if N<=(3*i**2+3*i+1):
            return i+1
print(beeHouse(int(input())))

'''

# 숏코딩 https://www.acmicpc.net/source/6380847

print(int((int(input())/3-.1)**.5+1.5))

'''