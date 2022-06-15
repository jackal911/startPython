# 소수 찾기 https://www.acmicpc.net/problem/1978
from math import sqrt

N = int(input())
sosu = [2, 3, 5, 7, 11]
nums = list(map(int, input().split()))
count = 0
for i in range(sosu[-1]+1, max(nums)+1):
        CD = []
        for j in sosu:
            if j>sqrt(i):
                break
            elif i%j==0:
                CD.append(True)
                break
            else:
                CD.append(False)
        if sum(CD)==0:
            sosu.append(i)
        # print(sosu)
for i in range(N):    
    if nums[i] in sosu:
        count += 1
        continue
print(count)

'''풀이1
from math import floor, sqrt

N = int(input())
nums = list(map(int, input().split()))
count = 0
for i in range(N):
    # print(f'{i+1}번째 숫자 : {nums[i]}')
    if nums[i]==1:
        continue
    else:
        j = 2
        if j > sqrt(nums[i]):
            count += 1
            # print(f'{nums[i]}는 소수이다! 현재 소수 개수 : {count}')
            continue
        while j <= sqrt(nums[i]):
            # print(f'{j}가 {nums[i]}의 소수인가? : {nums[i]%j==0}')
            if nums[i]%j==0:
                break
            if j==floor(sqrt(nums[i])):
                count+=1
                # print(f'{nums[i]}는 소수이다! 현재 소수 개수 : {count}')
            j += 1
print(count)
'''

'''

# 숏코딩 https://www.acmicpc.net/source/9357086

input();print(sum(all(n%j for j in range(2,n))*n>1for n in map(int,input().split())))

'''