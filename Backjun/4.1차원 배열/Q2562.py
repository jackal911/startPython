# 최댓값 https://www.acmicpc.net/problem/2562
print(i*2 for i in range(10))
nums = []
for _ in range(9):
    nums.append(int(input()))
print(max(nums))
print(nums.index(max(nums))+1)

'''

# 숏코딩 https://www.acmicpc.net/source/20576119

print(*max((int(input()),i+1)for i in range(9)))

# max 함수의 파라미터를 살펴보면 (input숫자, 순서) 구조의 튜플이 9개 생기가 된다. max는 튜플들 중에 최댓값을 찾을 때 첫번째 원소, 즉 input숫자만을 고려해서 return하나보다.
# tuple의 대소관계에 대해서 검색하니 첫번째 원소를 먼저 비교하고, 같다면 두번째 원소를 비교하고, 반복해서 보다 큰 원소가 먼저 나온 튜플을 "크다"라고 인식한다.
# 문제에서는 서로 다른 자연수라고 명시했기 때문에 위와 같은 방법을 쓸 수 있지만, 만약에 같은 "자연수를 허용하고 최댓값이 2개라면 먼저 나온 수를 출력하라" 라고 한다면 operator의 itemgetter라든지 max의 key 파라미터를 이용해야 했을 것이다.
# 참고 : https://stackoverflow.com/questions/5292303/how-does-tuple-comparison-work-in-python

'''