# 영수증 https://www.acmicpc.net/problem/5565
total = int(input())
for i in range(9):
    total -= int(input())
print(total)

'''

# 숏코딩 https://www.acmicpc.net/source/12144685

print(int(input())+eval('-int(input())'*9))

# eval 복습. exec는 '문'을 처리할 수 있고 eval은 '식'만 처리할 수 있다
# 당연히 for문 보다 짧아서 숏코딩에 썼겠지만, eval이나 exec를 진지하게 쓰는 사람이 있다면 미련해보일 것 같은 기분이 든다. 이유가 뭘까?
# 가독성도 가독성이지만 for문이 논리를 반복하는 것이라면 ' '*9 와 같은 방식은 단순히 문장을 반복하는 거라서 그런게 아닐까.

'''