# 빠른 A+B https://www.acmicpc.net/problem/15552
import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    print(sum(map(int, input().split())))
    
'''

# 숏코딩 https://www.acmicpc.net/source/20950723

for l in[*open(0)][1:]:print(sum(map(int,l.split())))

'''