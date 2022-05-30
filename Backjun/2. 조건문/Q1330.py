# 두 수 비교하기 https://www.acmicpc.net/problem/1330
A, B = map(int, input().split())
if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')
    
'''

# 숏코딩 https://www.acmicpc.net/source/14336628

a,b=map(int,input().split())
print(['><'[a<b],'=='][a==b])

# a<b가 True일땐 1, False일땐 0 값을 가지는걸 이용해서 string '><'의 index로 >또는 <를 뽑아내고 같은 원리로 a==b로 수열의 index를 가리킴
# 뭔가 싶어서 보다가 이해하고나니 참 기발하다는 생각이 들었다.

'''