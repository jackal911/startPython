# 단어 공부 https://www.acmicpc.net/problem/1157
def countMax(s:str):
    s = s.upper()
    if len(s)<2:
        return s
    arr = set()
    for i in range(65, 91):
        arr.add((s.count(chr(i)), chr(i)))
    arr = sorted(arr, reverse=True)
    if arr[0][0]==arr[1][0]:
        return '?'
    else:
        return arr[0][1]
print(countMax(input()))

'''

# 숏코딩 https://www.acmicpc.net/source/18664160

from statistics import*
try:t=mode(input().upper())
except:t='?'
print(t)

# statistics 모듈의 mode는 최빈값을 도출하는 함수인데 예전에는 최빈값이 여러개면 에러가 발생했나보다.
# 파이썬 3.8 버젼 이후로는 최빈값이 여러개면 가장 처음에 나온 최빈값이 return 된다. 
# 그래서 Mississipi를 넣으면 I가 return되므로 지금은 이 문제에선 쓸 수 없다.

'''
