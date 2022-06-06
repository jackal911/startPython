# 구구단 https://www.acmicpc.net/problem/2739
N = int(input())
for i in range(1, 10):
    print("{} * {} = {}".format(N, i, N*i))

'''

# 숏코딩 https://www.acmicpc.net/source/12926704

a=b=int(input());exec("print(a,'*',b//a,'=',b);b+=a;"*9)

# 참고 : https://nan491.tistory.com/entry/Python-3-eval-%ED%95%A8%EC%88%98%EC%99%80-exec-%ED%95%A8%EC%88%98 -- eval() 함수와 exec() 함수
# eval() : 문자열로 표현된 파이썬 식을 인수로 받아 파이썬 컴파일 코드로 변환. '식'만 처리 가능하며 '문'을 받으면 SyntaxError 발생
# exec() : 문자열로 표현된 문을 인수로 받아 파이썬 컴파일 코드로 변환.

# 문자열*9 하면 9번 반복함

'''