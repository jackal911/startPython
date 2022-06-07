# 나머지 https://www.acmicpc.net/problem/3052
nums = set()
for _ in range(10):
    nums.add(int(input())%42)
print(len(nums))

'''

# 숏코딩 https://www.acmicpc.net/source/22308323

print(len({int(i)%42for i in open(0)}))

'''