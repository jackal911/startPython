# 블랙잭 https://www.acmicpc.net/problem/2798
import itertools as i
N, M = map(int, input().split())
cardSet = list(i.combinations(list(map(int, input().split())), 3))
max = 0
for card in cardSet:
    if sum(card)<=M and sum(card)>max:
       max = sum(card)
print(max)

'''

# 숏코딩 https://www.acmicpc.net/source/41131376

from itertools import*
n,m,*l=map(int,open(0).read().split())
print(max(x for x in map(sum,combinations(l,3))if x<=m))

'''