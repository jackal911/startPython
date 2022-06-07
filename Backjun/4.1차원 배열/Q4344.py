# 평균은 넘겠지 https://www.acmicpc.net/problem/4344
C = int(input())
for _ in range(C):
    nums = list(map(float, input().split()))
    avg = sum(nums[1:])/nums[0]
    print("{:.3f}%".format(sum(map(lambda x: 1 if x>avg else 0, nums[1:]))/nums[0]*100))
    
'''

# 숏코딩 https://www.acmicpc.net/source/23112300

exec(int(input())*'b,*c=map(int,input().split());print(f"{sum(b*i>sum(c)for i in c)/b:.3%}");')

'''