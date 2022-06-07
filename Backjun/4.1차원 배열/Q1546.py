# 평균 https://www.acmicpc.net/problem/1546
N = int(input())
score = list(map(float, input().split()))
M = max(score)
for i in range(N):
    score[i] = score[i]/M*100
print(sum(score)/N)

'''

# 숏코딩 https://www.acmicpc.net/source/29974289

n,*l=map(int,open(0).read().split())
print(sum(l)*100/n/max(l))

'''