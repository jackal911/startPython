# 별 찍기 - 1 https://www.acmicpc.net/problem/2438
N=int(input());a="";exec("a+='*';print(a);"*N)

'''

# 숏코딩 https://www.acmicpc.net/source/5840236

for i in range(int(input())):print('*'*-~i)

# 참고 : https://www.acmicpc.net/board/view/40946 *-~ 에 대한 질의응답
# ~ : 2의 보수 표기법. ~x = -x-1. 따라서 -~i = -(-i-1) = i+1이 된다.

'''