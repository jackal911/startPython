# 체스판 다시 칠하기 https://www.acmicpc.net/problem/1018
# import time
# start = time.time()

N, M = map(int, input().split())
chessBoard = []  # input되는 체스판이 들어갈 list
for _ in range(N):
    inp = input()
    inp = inp.replace('B', '0')
    inp = inp.replace('W', '1')  # 편의상 B, W 대신 0, 1을 사용한다.
    chessBoard.append(inp)
# print(chessBoard)
minNum = 1250  # 최솟값 출력할 변수. 나올 수 있는 최댓값인 1250으로 시작
toggleNum = 0  # 1과 0이 번갈아서 나온다.
for i in range(N-7):  # 시작행 루프
    for j in range(M-7):  # 시작열 루프
        countA = 0  # 바꿔야할 색깔 개수를 count하는 변수
        countB = 0  # A 버전과 B 버전은 시작 색깔 차이
        for m in range(i, i+8):  # 여덟행 순회 루프
            for k in range(j, j+8):  # 여덟열 순회 루프 A 버전
                if chessBoard[m][k] != str(toggleNum):  # input된 체스보드 색이 원래 들어가야될 색과 다르면
                    countA += 1  # 바꿔야 할 색깔 개수를 +1한다.
                toggleNum ^= 1  # 0이면 1로, 1이면 0으로
            toggleNum ^= 1  # B버전을 시작하기 위해 색을 조정한다.
            for k in range(j, j+8):  # 여덟열 순회 루프 B 버전
                if chessBoard[m][k] != str(toggleNum):
                    countB += 1
                toggleNum ^= 1  # 0이면 1로, 1이면 0으로
        minNum = min(minNum, min(countA, countB))  # 기존의 최솟값과 A버전, B버전 모두를 비교해서 최솟값을 갱신한다.
print(minNum)  # 최솟값 출력

# print("time : ", time.time() - start)

'''

# 숏코딩 https://www.acmicpc.net/source/28531560

n,m=map(int,input().split())
*d,=map(input,['']*n)
e=[sum(sum(a==b for a,b in zip(k,l[j:]))for k,l in zip(['WB'*4,'BW'*4]*4,d[i:]))for j in range(m-7)for i in range(n-7)]
print(min(min(e),64-max(e)))

'''