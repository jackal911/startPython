# 주사위 https://www.acmicpc.net/problem/9295
for i in range(int(input())):
    print("Case %d: %d" % (i+1, sum(map(int, input().split()))))
    

'''

# 숏코딩 https://www.acmicpc.net/source/28743550

for i in range(int(input())):print(f"Case {i+1}:",eval('+'.join(input())))

# input()은 string으로 들어오는데 join으로 +를 넣고 eval을 거치니 x+y가 연산된다.
# 신기해서 테스트해봤더니 eval('+'.join(['3', '4'])) = 7이 나오더라.
# eval 함수가 식을 만들어주는 줄은 알고 있었지만 이정도로 유연할 줄은 몰랐다. 말 그대로 string을 넣으면 식이 만들어지는 거라는게 새삼 실감났다.

'''
