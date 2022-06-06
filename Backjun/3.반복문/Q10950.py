# A+B - 3 https://www.acmicpc.net/problem/10950
# T = int(input())
# for i in range(T):
#     A, B = map(int, input().split())
#     print(A+B)
for a,_,c,_ in[*open(0)][1:]:
    print(int(a)+int(c))
'''

# 숏코딩 https://www.acmicpc.net/source/20883561

for a,_,c,_ in[*open(0)][1:]:print(int(a)+int(c))

# ??????? 문제랑 맞는 답인지 모르겠다. 입력값을 넣어도 출력이 되지 않는다.

# 언더바(_) 사용하기 - 출처 : https://gomguard.tistory.com/125
# 1. 인터프리터에서 마지막 값을 저장하고 싶을 때 사용. (X)
# 2. 값을 무시하고 싶을 때 사용. (O)
# - a,_,c,_ 의 경우에는 in 다음에 오는 2번째 값과 4번째 값은 무시하고 1번째의 a, 2번째의 c 자리에 있는 수만 고려한다는 의미인 듯.
# 3. 어떤 것에 특별한 의미를 부여하고 싶을 때 사용할 수 있다. (X) ex) __init__.py라는 파일이 있으면 그 폴더를 패키지로 만들 수 있다.
# 4. 숫자 또는 문자값의 자릿수 구분을 위한 구분자로써 사용. (X) ex) 1_000_000은 출력이나 연산시에 1000000으로 처리된다. 개발자의 편의를 위한 기능인 듯.

'''