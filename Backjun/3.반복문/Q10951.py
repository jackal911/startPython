# A+B - 4 https://www.acmicpc.net/problem/10951
while(True):
    try:
        print(sum(map(int, input().split())))
    except EOFError:
        break
# EOFError(End Of File)를 처리하는 문제

'''

# 숏코딩 https://www.acmicpc.net/source/20866422

for l in open(0):print(eval(l[0]+'+'+l[2]))

# open(0)도 여러줄을 한번에 입력받는거라 그런지 EOFError를 피할 수 있는듯하다.

'''