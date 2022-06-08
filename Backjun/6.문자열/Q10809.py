# 알파벳 찾기 https://www.acmicpc.net/problem/10809
alphabets = input()
for i in range(97, 123):
    try:
        print(alphabets.index(chr(i)), end=" ")
    except ValueError:
        print(-1, end=" ")
        continue

'''

# 숏코딩 https://www.acmicpc.net/source/4908366

print(*map(input().find,map(chr,range(97,123))))

# find는 없으면 -1을 return한다. index는 오류를 일으키니 쓸거면 find를 써야겠다.

'''    
