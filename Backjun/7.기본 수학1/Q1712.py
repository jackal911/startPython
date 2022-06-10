# 손익분기점 https://www.acmicpc.net/problem/1712
A, B, C = map(int, input().split())
if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)
    
'''

# 숏코딩 https://www.acmicpc.net/source/5357493

a,b,c=map(int,input().split());print(-(c<=b)or a//(c-b)+1)

# or은 왼쪽부터 참 거짓(0)을 따진다. 왼쪽이 참이면 출력하고 거짓(0)이면 오른쪽의 참 거짓을 판별한다.

'''