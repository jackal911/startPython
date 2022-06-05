# 더하기 사이클 https://www.acmicpc.net/problem/1110
result = N = int(input())
cycle = 1
# :=의 쓰임을 알기 전의 풀이
# result = (N%10)*10 + (N//10+N%10)%10
# while result!=N:
#     result = (result%10)*10 + (result//10+result%10)%10
#     cycle += 1
while (result := (result%10)*10 + (result//10+result%10)%10)-N:
    cycle += 1
print(cycle)

'''

# 숏코딩 https://www.acmicpc.net/source/25242586

a=n=int(input());c=1
while(a:=a%10*10+a*11//10%10)-n:c+=1
print(c)

# := 의 의미가 java에서의 do-while 이자 루프가 돌때마다 그 문장을 실행한다는 의미라는 걸 알았다.
# 2번 정의하는 번거로움을 없애주고 반복문의 목적을 뚜렷하게 보여줘서 잘 쓰면 요긴하겠다.

'''