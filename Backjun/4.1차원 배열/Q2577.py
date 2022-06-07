# 숫자의 개수 https://www.acmicpc.net/problem/2577
nums = []
for _ in range(3):
    nums.append(int(input()))
mul = str(nums[0]*nums[1]*nums[2])
for i in range(10):
    print(mul.count(str(i)))
    
'''

# 숏코딩 https://www.acmicpc.net/source/16403204

exec('n,m=0,1'+'*int(input())'*3+';print(str(m).count(str(n)));n+=1'*10)

'''