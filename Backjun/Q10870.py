# 피보나치 수 5 https://www.acmicpc.net/problem/10870
def pibo(N: int):
    if N<=1:
        return N
    else:
        return pibo(N-1) + pibo(N-2)
print(pibo(int(input())))

'''

# 숏코딩 https://www.acmicpc.net/source/16169732

a=0;b=1
exec("a,b=b,a+b;"*int(input()))
print(a)

'''