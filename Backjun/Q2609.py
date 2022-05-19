# 최대공약수와 최소공배수 https://www.acmicpc.net/problem/2609
from math import gcd, lcm

a, b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))

'''

# 숏코딩 https://www.acmicpc.net/source/3413679

a,b=map(int,input().split());L=a*b
while b:a,b=b,a%b
print(a,L//a)

# 최소공배수와 최대공약수 관계 이용

'''