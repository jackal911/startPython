# 별 찍기 - 2 https://www.acmicpc.net/problem/2439
N = int(input())
star = ""
for i in range(N):
    star += "*"
    
    # output = "{:>"+str(N)+"}".format(star) # 미리 format 함수를 사용하면 인식을 못한다.    
    output = "{:>"+str(N)+"}" # 내가 찾은 방법    
    print(output.format(star))
    
    # output = "{:>{}}".format(star, N) # 숏코딩 통해서 얻은 아이디어
    # print(output)



'''

# 숏코딩 https://www.acmicpc.net/source/20886030

i,n=0,int(input()) # i=0, n=int(input())
while n-i:i+=1;print(f'{"*"*i:>{n}}')

# 중괄호를 중복으로 사용해서 자리수 지정을 변수로 할 수 있음
# 숏코딩에서는 f-string으로 사용했지만 format 함수로 사용하게 되면 중괄호가 열린 순서대로 매개변수를 입력해야함
# 짧게하려고 그런거겠지만 변수 할당을 괄호없이 튜플로 하는건 보기 좋은 방법은 아닌듯
# while n-i 같은 형식은 실제로 선호될지 모르겠지만 저런것도 있구나 싶었음

'''