# 셀프 넘버 https://www.acmicpc.net/problem/4673
r = range(100)
def d(n:int):
    selfNum = n+n%10+(n%100)//10+(n%1000)//100+(n%10000)//1000+n//10000
    return selfNum
nums = list(range(1,10001))
for n in range(1, 10001):
    try:
        nums.remove(d(n))
    except ValueError:
        continue
print(*nums)

'''

# 숏코딩 https://www.acmicpc.net/source/6011096

r=range(9999);print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))

# 자릿수 더하는 걸 sum(map(int, str(n))) 로 처리한게 인상적이다.
# *을 이용해서 set을 한번에 선언하는 것, set끼리 뺄셈을 하면 차집합이 된다는 것도 활용가치가 있을 것 같다.

'''