# 별 찍기 - 8 https://www.acmicpc.net/problem/2445
N = int(input())
for i in range(-N+1, N):
    real_i = abs(i)
    print("*"*(N-real_i)+" "*2*real_i+"*"*(N-real_i))


'''

# 숏코딩 https://www.acmicpc.net/source/22353837

n=int(input())
for i in range(-n+1,n):print((' '*abs(2*i)).center(2*n,'*'))

# a.center(b, c) : 전체 공간의 너비를 b만큼으로 잡고 문자열 a를 중앙정렬 시킨뒤 나머지 공간인 양 옆을 c로 채우겠다는 뜻
# ex) "abc".center(9, "-") -> ---abc---

'''