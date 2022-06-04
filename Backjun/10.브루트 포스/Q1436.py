# 영화감독 숌 https://www.acmicpc.net/problem/1436
import time
start = time.time()

N = int(input())  # N번째 숫자를 구할 것이다.
nums = []  # 숫자들이 들어갈 list
for i in range(6668):  # 넉넉하게. 앞뒤로 6이 붙을때 대소관계가 뒤집혀서 6667까지 포함하도록 잡은것뿐이다.
    numStr = str(i)  # 숫자 i를 string으로 변환한다.
    for j in range(len(numStr)+1):  # 0부터 i번째 숫자의 자릿수만큼 순회하는데 그 이유는
        numLast = numStr[:j] + "666" + numStr[j:]  # 666의 앞뒤로 골고루 숫자가 들어가게 하기 위해서다.
        nums.append(int(numLast))
for j in range(2, 4):  # 위 루프에서 놓치는 케이스가 생겨서 넣는다.
    for k in range(102):
        numStr = "666" + "{:0>{}}".format(str(k), j)  # k라는 숫자를 넣되 j만큼의 공간을 가지고 빈칸은 0으로 채운다.
        nums.append(int(numStr))
nums = set(nums)  # 중복을 없애는 작업
nums = list(nums)  # 다시 list로 바꾼다
nums.sort()  # 오름차순 정렬한다.
# print(nums)
print(nums[N-1])  # N번째 수를 구하기 위해서 N-1번째 element를 찾는다.

print("걸린시간 : ", time.time()-start)

'''

# 숏코딩 https://www.acmicpc.net/source/18359621

print([i for i in range(9**7)if"666"in str(i)][int(input())-1])

'''