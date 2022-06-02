# 체스판 다시 칠하기 https://www.acmicpc.net/problem/1018
# import time
# start = time.time()

N, M = map(int, input().split())
chessBoard = []
for _ in range(N):
    inp = input()
    inp = inp.replace('B', '0')
    inp = inp.replace('W', '1')
    chessBoard.append(inp)
# print(chessBoard)
minNum = 1250  # 최솟값 출력할 변수. 나올 수 있는 최댓값인 1250으로 시작
toggleNum = 0
for i in range(N-7):  # 시작행 루프
    for j in range(M-7):  # 시작열 루프
        countA = 0
        countB = 0
        for m in range(i, i+8):  # 8행 순회 루프            
            for k in range(j, j+8):  # 8열 순회 루프
                if chessBoard[m][k] != str(toggleNum):
                    countA += 1
                toggleNum ^= 1  # 0이면 1로, 1이면 0으로
            toggleNum ^= 1  # 밑에꺼는 위에꺼와 반대로
            for k in range(j, j+8):
                if chessBoard[m][k] != str(toggleNum):
                    countB += 1
                toggleNum ^= 1  # 0이면 1로, 1이면 0으로
        minNum = min(minNum, min(countA, countB))
print(minNum)

# print("time : ", time.time() - start)

'''

# 숏코딩 https://www.acmicpc.net/source/28531560

n,m=map(int,input().split())
*d,=map(input,['']*n)
e=[sum(sum(a==b for a,b in zip(k,l[j:]))for k,l in zip(['WB'*4,'BW'*4]*4,d[i:]))for j in range(m-7)for i in range(n-7)]
print(min(min(e),64-max(e)))

'''