# 그룹 단어 체커 https://www.acmicpc.net/problem/1316
def checker(s:str):
    st = set(s)
    save = ""
    for ch in s:        
        if ch!=save:
            save = ch
            try:
                st.remove(ch)
            except KeyError: # 문자열에는 포함돼있지만 이미 set에선 빠진 상태. 즉 같은 문자가 떨어져있는 상태에서 KeyError가 발생한다.
                return 0
    return 1

N = int(input())
count = 0
for _ in range(N):
    count += checker(input())
print(count)

'''

# 숏코딩 https://www.acmicpc.net/source/27499365

print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)

'''