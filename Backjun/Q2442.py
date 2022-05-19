# 별 찍기 - 5 https://www.acmicpc.net/problem/2442
N = int(input())
blank = " "*N
stars = "*"
for _ in range(N):
    blank = blank.removesuffix(" ")    
    print(blank+stars)
    stars += "**"
    
'''

# 숏코딩 https://www.acmicpc.net/source/30392761

a=int(input());b=1;
while a:print((a-1)*' '+b*'*');a-=1;b+=2

'''