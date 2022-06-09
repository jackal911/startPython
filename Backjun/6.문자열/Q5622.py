# 다이얼 https://www.acmicpc.net/problem/5622
time = 0
alph = input()
for ch in alph:
    if ch<'D':
        time += 3
    elif ch<'G':
        time += 4
    elif ch<'J':
        time += 5
    elif ch<'M':
        time += 6
    elif ch<'P':
        time += 7
    elif ch<'T':
        time += 8
    elif ch<'W':
        time += 9
    else:
        time += 10
print(time)

'''

# 숏코딩 https://www.acmicpc.net/source/18666939

print(sum(5*min(ord(x),88)//16-17for x in input()))

'''
