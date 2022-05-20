# 별 찍기 - 9 https://www.acmicpc.net/problem/2446
N = int(input())
for i in range(-N+1, N):
    real_i = abs(i)
    print(" "*(N-real_i-1)+"*"*(2*real_i+1))


'''

# 숏코딩

n=int(input())
for i in map(abs,range(1-n,n)):print(' '*(n-i-1)+"*"*(2*i+1))

# map을 이용해서 절대값 함수를 range에 뿌려주는거 확인
# 다른 숏코딩에 비해 유일하게 1바이트 작은 이유는 -n+1과 1-n 차이라는거 ㅋㅋ

'''