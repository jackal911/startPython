# 별 찍기 - 3 https://www.acmicpc.net/problem/2440
N = int(input())
star = "*"*N
for i in range(N):
    print(star)
    star = star.removesuffix("*")

# removesuffix(str: str) : 마지막 문자가 str과 같으면 제거한 문자열을 return하고 다르면 원래 문자열을 return한다.
# removeprefix(str: str) : 첫 문자가 ~상동

'''

# 숏코딩 https://www.acmicpc.net/source/23119042

n=int(input())
while n:print(n*"*");n-=1

# n 값을 직접 움직여서 별 개수를 통제함

'''