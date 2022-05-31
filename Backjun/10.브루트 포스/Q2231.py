# 분해합 https://www.acmicpc.net/problem/2231
# print(sum(map(int, list(str(1234)))))
N = int(input())
i=0
hab=0
while i<N:
    i += 1
    hab = i + sum(map(int, list(str(i))))
    # print(hab)
    if hab==N:
        print(i)
        break
if i==N:
    print(0)
        
'''

# 숏코딩 https://www.acmicpc.net/source/20879959

n=int(input())
print([*[i for i in range(n)if n==i+sum(map(int,str(i)))],0][0])

# list를 안 씌워도 되는구나.

'''