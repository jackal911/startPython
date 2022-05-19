# 피보나치 수 2 https://www.acmicpc.net/problem/2748
n = int(input())
pibo = [0, 1]
for i in range(2, n+1):
    pibo.append(pibo[i-1] + pibo[i-2])
print(pibo[n])

'''

# 숏코딩 https://www.acmicpc.net/source/5836637

a,b=0,1;exec("a,b=b,a+b;"*int(input()));print(a)

'''