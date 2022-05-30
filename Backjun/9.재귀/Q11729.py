# 하노이 탑 이동 순서 https://www.acmicpc.net/problem/11729
def jangdae(n: int, start: int, end: int):
    if n==1:
        print(start, end)
        return    
    jangdae(n-1, start, 6-start-end)
    print(start, end)
    jangdae(n-1, 6-start-end, end)
    
N = int(input())
print(2**N-1)
jangdae(N, 1, 3)

'''

# 숏코딩 

def h(f,t,n):n>1!=h(f,f^t,n-1);print(f,t);n>1!=h(f^t,t,n-1)
n=int(input());print(2**n-1);h(1,3,n)

# 비트 연산자 ^ 를 이용해서 1, 2, 3 중 빠진 나머지 1개를 선택할 수 있다는게 신기하다. 1^3 = 2 1^2 = 3 2^3 = 1.
# 보다보니 XOR 연산을 하는 2개의 변수와 그 결과값까지 3개는 서로 XOR 연산안에서 순환하는 것을 알게됐다. ex) 13 ^ 9 = 4, 13 ^ 4 = 9, 4 ^ 9 = 13

'''

'''시도1
def jangdae(N: int, arr: list, holjjack=True):
    if N==1:
        arr.append('1 3') if holjjack==False else arr.append('1 2')
        return 1
    # if i==1:
    #     move = 3 if N%2==0 else 2
    #     print(i, move)
    return 2*(jangdae(N-1, arr))+1
N = int(input())
holjjack = True if N%2==0 else False
arr = []
print(jangdae(N, arr))
print(arr)
'''