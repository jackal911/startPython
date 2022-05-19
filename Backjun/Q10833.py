# 사과 https://www.acmicpc.net/problem/10833
N = int(input())
remain = 0
for _ in range(N):
    school, apple = map(int, input().split())
    remain += apple%school
print(remain)

'''

# 숏코딩 https://www.acmicpc.net/source/9821462

s=0;exec("a,b=map(int,input().split());s+=b%a;"*int(input()));print(s)

'''