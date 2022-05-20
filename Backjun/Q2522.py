# 별 찍기 - 12 https://www.acmicpc.net/problem/2522
N = int(input())
for i in range(-N+1, N):
    starNum = abs(i)
    print(" "*starNum+"*"*(N-starNum))
    
'''

# 숏코딩 https://www.acmicpc.net/source/39794368

n=int(input())
i=-n+1
while i<n:print(f"{' '*abs(i):*<{n}}");i+=1

# 자릿수를 n개로 제한하여 공백을 먼저 넣고 나머지 자릿수를 *로 채우는 방식

'''