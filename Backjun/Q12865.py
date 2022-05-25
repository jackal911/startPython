# 평범한 배낭 https://www.acmicpc.net/problem/12865
# 일단 input()으로 최대한 시간복잡도를 줄여보고 안되면 stdin을 써볼 예정
# N, K = map(int, input().split())
# things = [[0, 0]]
# for _ in range(N):
#     W, V = map(int, input().split())
#     things.append([W, V])
# knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     for j in range(1, K+1):
#         weight = things[i][0]
#         value = things[i][1]
#         if j<weight:
#             knapsack[i][j] = knapsack[i-1][j]
#         else:
#             knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])
# print(knapsack[N][K])

m,r=lambda:map(int,input().split()),range
n,k=m()
d=[0]*(k+1)
print(d)
for _ in r(n):
    w,v=m()
    for i in r(k,w-1,-1):d[i]=max(d[i],d[i-w]+v)
    print(d)
print(d)
print(d[k])


'''

# 숏코딩 https://www.acmicpc.net/source/38314236

m,r=lambda:map(int,input().split()),range
n,k=m()
d=[0]*(k+1)
for _ in r(n):
    w,v=m()
    for i in r(k,w-1,-1):d[i]=max(d[i],d[i-w]+v)
print(d[k])

# 냅색 알고리즘에서 어차피 바로 전 행과만 상호작용하는 걸 이용해서 덮어쓰기하며 1차원으로 구현한 것
# 냅색을 충분히 공부해서 그나마 알아보지 아니면 외계어로 느껴졌을 듯

'''


''' 시도1
import copy

N, K = map(int, input().split())
lst = dict()
for _ in range(N):
    w, k = map(int, input().split())
    if not lst.get(w, False):  # lst의 key 값중 w가 없으면 실행. value값이 0일때도 not 0 = true 이므로 실행된다. 이는 물건의 가치의 최소값이 0이므로 덮어써도 무관하다.
        lst[w] = k
    elif lst[w] < k:  # 기존에 key 값에 대한 value를 가지고 있지만 이번 input의 value값이 더 클 경우에는 덮어쓴다. if문에 or로 잇지 않고 elif로 따로 떼어놓은 이유는 python에서 or문을 썼을때 앞의 boolean이 True라고 하더라도 뒤의 boolean을 체크 할 지 모르기 때문이다. 문제를 먼저 풀고나면 확인 해 볼 것이다.
        lst[w] = k
# print(lst.items())
max = 0  # 최대값 넣을 곳
for key, val in lst.items():  # key는 무게, val은 가치의 변수
    print('처음 key: {}, 처음 val: {}'.format(key, val))
    lstTemp = copy.deepcopy(lst)  # deepcopy를 해야 별도로 pop을 해도 원래 dict에 변화가 없다.
    lstTemp.pop(key)
    for i in range(1, K-key+1):  # 따라서 K < w이면 for문을 바로 빠져나오게 된다.
        print(f'현재 i: {i}')
        if lstTemp.get(i):  # 무게가 i인 물건이 있으면
            print(f'더할 무게: {i}, 더할 가치: {lstTemp[i]}')
            key += i
            val += lstTemp[i]
            print('현재 key: {}, 현재 val: {}'.format(key, val))
        if key >= K:
            break
    if val > max and key <= K:  # 현재 합산한 가치가 max보다 크면 max로 등극한다.
        max = val
print(max)
'''

''' 시도2
import copy

def maxCal(thisWeight: int, dict: dict, maxWeight: int, curTotalWeight: int):
    whoIsMax = []
    if thisWeight>maxWeight:
        return 0
    elif thisWeight==maxWeight:
        return dict[curTotalWeight]
    else:        
        dictTemp = copy.deepcopy(dict)
        dictTemp.pop(thisWeight)
        for weight in dict.keys():
            continue            
        
lst = dict()  # test
lst[1] = 2
print(lst)
maxCal(1, lst)
print(lst)

N, K = map(int, input().split())
lst = dict()
for _ in range(N):
    w, k = map(int, input().split())
    if not lst.get(w, False):  # lst의 key 값중 w가 없으면 실행. value값이 0일때도 not 0 = true 이므로 실행된다. 이는 물건의 가치의 최소값이 0이므로 덮어써도 무관하다.
        lst[w] = k
    elif lst[w] < k:  # 기존에 key 값에 대한 value를 가지고 있지만 이번 input의 value값이 더 클 경우에는 덮어쓴다. if문에 or로 잇지 않고 elif로 따로 떼어놓은 이유는 python에서 or문을 썼을때 앞의 boolean이 True라고 하더라도 뒤의 boolean을 체크 할 지 모르기 때문이다. 문제를 먼저 풀고나면 확인 해 볼 것이다.
        lst[w] = k
'''

