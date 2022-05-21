# 플러그 https://www.acmicpc.net/problem/2010
from sys import stdin

N = int(input())
print(sum(int(stdin.readline())-1 for _ in range(N))+1)  # input() 보다 stdin.readline()이 훨씬 빠르다

'''

# 숏코딩 https://www.acmicpc.net/source/25821289

n = [*map(int,open(0))]
print(sum(n[1:])-n[0]+1)

# open(0)로 전체 input을 다 받아 list에 넣은 다음에 1번째 int부터 끝까지 다 더하고 플러그 개수인 0번쨰 int를 뺀다음에 1개를 더한다.
# open(0)의 데이터 input방식은 찾아봐도 아직도 잘 모르겠다.
# 속도 줄이기를 하다보니 numba나 PyPy에 대한 얘기가 많이 나오더라. 공부해야될듯

'''
