# 상수 https://www.acmicpc.net/problem/2908
nums = list(input())
nums.reverse()
print(max(map(int, ''.join(nums).split())))

'''

# 숏코딩 https://www.acmicpc.net/source/435052

print(max(input()[::-1].split()))

# input()[::-1] - input() 문자열의 전체를 조회하되 ([:]) -1씩 더하면서 조회해라[::-1] 는 뜻이다. 간단해서 사용성이 높을것같다.

'''