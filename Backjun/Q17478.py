# 재귀함수가 뭔가요? https://www.acmicpc.net/problem/17478
def jaegui(N: int, i=0):
    bars = '_'*(i*4)    
    print(f'''{bars}"재귀함수가 뭔가요?"''')
    if i<N:
        print(f'''{bars}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
{bars}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
{bars}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."''')
        jaegui(N, i+1)
    else:
        print(f'{bars}"재귀함수는 자기 자신을 호출하는 함수라네"')
    print(f'{bars}라고 답변하였지.')
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
jaegui(int(input()))

"""

# 숏코딩 https://www.acmicpc.net/source/34191457

p=print
def r(i):
	s='____'*i;p(s+'"재귀함수가 뭔가요?"')
	if i==n:p(s+'"재귀함수는 자기 자신을 호출하는 함수라네"')
	else:p(f'''{s}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
{s}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
{s}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."''');r(i+1)
	p(s+'라고 답변하였지.')
n=int(input())
p('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
r(0)

"""