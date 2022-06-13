# ACM 호텔 https://www.acmicpc.net/problem/10250
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    print("{}{:02d}".format(N%H if N%H!=0 else H, N//H+1 if N%H!=0 else N//H))

'''

# 숏코딩 https://www.acmicpc.net/source/35843095

for r in[*open(0)][1:]:h,_,n=map(int,r.split());n-=1;print((n%h+1)*100+n//h+1)

'''