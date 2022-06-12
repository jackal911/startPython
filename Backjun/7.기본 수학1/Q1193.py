# 분수찾기 https://www.acmicpc.net/problem/1193
X = int(input())
i = 0
while True:
    i += 1
    maxNum = i*(i+1)//2
    if X<=maxNum:
        if i%2==1:
            print(f"{maxNum-X+1}/{i-maxNum+X}")
        else:
            print(f"{i-maxNum+X}/{maxNum-X+1}")
        break
    
'''

# 숏코딩 https://www.acmicpc.net/source/27657152

n=int(input());a=0
while n>0:a+=1;n-=a
print("%d/%d"%(1-n,a+n)[::a%2*2-1])

# a는 1씩 늘리고 n은 a씩 줄여가며 몇번째 열인지 도출하는 과정이 인상적이다.

'''