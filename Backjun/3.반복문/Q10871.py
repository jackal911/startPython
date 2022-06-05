# X보다 작은 수 https://www.acmicpc.net/problem/10871
N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []
# print(*(a for a in A if a<X))
for a in A:
    if a<X:
        result.append(a)
print(*result)

'''

# 숏코딩 https://www.acmicpc.net/source/4897948

N,X=input().split();print(*(t for t in input().split()if int(t)<int(X)))

# if문과 for문을 함께 쓸때는 for문을 먼저 쓰고 if를 써야된다.

'''