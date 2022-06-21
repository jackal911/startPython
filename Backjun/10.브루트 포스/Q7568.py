# 덩치 https://www.acmicpc.net/problem/7568
N = int(input())
lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
result = ""
for i in range(N):
    rank = 1
    for j in range(N):
        # print(lst[i], "vs", lst[j])
        if lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1]:
            rank += 1
    # print(rank, end = " ")
    result += str(rank)
print(*result)  # 실패1
# print(" ".join(result))  # 실패2

'''시도1

from operator import itemgetter
N = int(input())
people = list()  # 사람들 몸무게, 키 담을 곳
for _ in range(N):
    people.append(tuple(map(int, input().split())))  # 몸무게와 키를 tuple 형식으로 append
orderedPeople = sorted(people, key=itemgetter(1))
orderedPeople = sorted(orderedPeople, key=itemgetter(0), reverse=True)  # 몸무게순으로 내림차순 정렬

print(orderedPeople)
rankPeople = dict()  # 순위 매길 딕셔너리
rankPeople[orderedPeople[0]] = 1  # 1등을 먼저 매긴다
for i in range(1, N):
    if orderedPeople[i][1]>=orderedPeople[i-1][1] or orderedPeople[i][0]==orderedPeople[i-1][0]:  # 몸무게가 더 적은 뒷 사람이 키가 더 크거나 같다면
        rankPeople[orderedPeople[i]] = rankPeople[orderedPeople[i-1]]  # 이전 사람과 동순위를 매긴다
    else:  # 반대로 몸무게가 적으면서 키도 작다면
        rankPeople[orderedPeople[i]] = i+1  # 현재 순서에 맞는 순위를 매긴다
result = ""
for person in people:
    result += str(rankPeople[person]) + " "
print(result)

'''

'''

# 숏코딩 https://www.acmicpc.net/source/28613583

v=[[*map(int,input().split())]for _ in[0]*int(input())]
for a,b in v:print(1+sum((a<c)*(b<d)for c,d in v))

'''
