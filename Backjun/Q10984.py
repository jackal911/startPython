# 내 학점을 구해줘 https://www.acmicpc.net/problem/10984
# T = int(input())
# for i in range(T):
#     N = int(input())
#     hakjum = 0
#     score = 0
#     for j in range(N):
#         inp = input().split()
#         C = int(inp[0])
#         G = float(inp[1])
#         hakjum += C
#         score += G*C
#     print(hakjum, "{:.1f}".format(score/hakjum))
    
N,I=int,input
for _ in[0]*N(I()):
    c=g=0
    for _ in[0]*N(I()):a,b=map(float,I().split());c+=a;g+=a*b
    print(N(c),'%.1f'%(g/c))
    
'''

# 숏코딩 https://www.acmicpc.net/source/11677034

i=input;exec('t,a=0,0;exec("c,s=map(float,i().split());t+=c;a+=c*s;"*int(i()));print("%d %.1f"%(t,a/t));'*int(i()))

# i()가 뭔가 했더니 input 글자 줄일려고 저렇게 한 듯
# 딱히 배울점은 없음

'''