# 최소, 최대 https://www.acmicpc.net/problem/10818
N = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))

# nums = map(int, input().split())
# 5
# 20 10 35 30 7 입력
# print(min(nums), max(nums))
# min() arg is an empty sequence 오류 뜸

# 그래서 실험 시작

# 실험1
# print(*nums)
# print(*nums)
# 결과 :
# 20 10 35 30 7
# (빈 행으로 출력)
# 그냥 출력만 했을뿐인데 왜 없어질까?

# 실험2
# print(nums)
# print(nums)
# 결과 :
# <map object at 0x0000023D80E2E370>
# <map object at 0x0000023D80E2E370>
# 단순 출력은 안 없어짐

# 실험3
# print(list(nums))
# print(list(nums))
# 결과 :
# [20, 10, 35, 30, 7]
# []
# list로 출력 후에도 없어짐

# 참고 : https://bluese05.tistory.com/56
# map 객체는 generator객체와 같이 불러낼때마다 메모리 적재되고 한번 사용하면 사라지는 객체인듯 하다. 
# 아래 코드를 실행해보면 generator 보다 더 적은 메모리를 map객체가 사용하고 있음을 알 수 있다.
# import sys
# print(sys.getsizeof( [i for i in range(100) if i % 2] ))
# print(sys.getsizeof( [i for i in range(1000) if i % 2] ))
# print(sys.getsizeof( (i for i in range(100) if i % 2) ))
# print(sys.getsizeof( (i for i in range(1000) if i % 2) ))
# print(sys.getsizeof(map(int, (i for i in range(1000)))))
# a = map(int, (i for i in range(1000)))
# print(*a)
# print(*a)  # a가 비어있다.