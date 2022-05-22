# 할로윈의 사탕 https://www.acmicpc.net/problem/10178
# for _ in range(int(input())):
#     c, v = map(int, input().split())
#     print(f"You get {c//v} piece(s) and your dad gets {c%v} piece(s).")

print(*divmod(*map(int,input().split())))

for _ in [0]*int(input()):
    print('You get {0} piece(s) and your dad gets {1} piece(s).'.format(*divmod(*map(int,input().split()))))

'''

# 숏코딩 https://www.acmicpc.net/source/17685044

for _ in [0]*int(input()):
    print('You get %d piece(s) and your dad gets %d piece(s).'%divmod(*map(int,input().split())))

# % 포맷팅에 divmod로 몫과 나머지를 tuple로 return 하여 문장을 완성한다.
# format 함수로 변형하면 다음과 같다
for _ in [0]*int(input()):
    print('You get {0} piece(s) and your dad gets {1} piece(s).'.format(*divmod(*map(int,input().split()))))
# format 함수에선 다중변수를 parameter로 사용하므로 divmod의 return값인 tuple에 *을 넣어 가변인자로 변형해야한다.

'''