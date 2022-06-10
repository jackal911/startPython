# 단어 공부 https://www.acmicpc.net/problem/1157
def countMax(s:str):  # 최빈 알파벳 return 하는 함수
    s = s.upper()  # 대문자로 바꾸고 시작
    if len(s)<2:  # 1글자면 바로 return하고 프로그램 종료. 뒤에서 indexerror 발생시키는 것 방지.
        return s
    arr = list()  # A~Z에 대해 (알파벳 개수, 알파벳)을 tuple형식으로 저장할 set
    for i in range(65, 91):  # 65~90은 아스키코드로 A~Z를 의미한다.
        arr.append((s.count(chr(i)), chr(i)))  # 빈도수를 tuple의 0번 index에 넣은 이유는 tuple이 정렬될 때 0번째 인덱스부터 차례대로 비교하기 때문이다.
    # for i in range(len(s)):
    #     arr.append((s.count(s[i]), s[i]))
    print(arr)
    arr = sorted(arr, reverse=True)  # 빈도수를 내림차순으로 정렬한다. 즉 0번째 알파벳은 최빈 알파벳이다.
    print(arr)
    if arr[0][0]==arr[1][0]:  # 최빈이 2개 이상인지 확인
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
