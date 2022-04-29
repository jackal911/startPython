# N 찍기 https://www.acmicpc.net/problem/2741
N = int(input())
for i in range(N):
    print(i+1)

'''

# 숏코딩 https://www.acmicpc.net/source/7927519

print(*range(1,int(input())+1))

# Asterisk(*) 이해하기 https://mingrammer.com/understanding-the-asterisk-of-python/
# 위 코드에선 컨테이너 타입 데이터 unpacking의 의미로 사용한듯 함
# * 로는 tuple과 list등 iterable한 데이터에 대해 unpacking 가능. range도 마찬가지
# dict 타입 unpacking은 **을 사용
# 가변인자 사용에 대한 내용도 중요해보임

'''