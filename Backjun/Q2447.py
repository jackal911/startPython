# 별 찍기 - 10 https://www.acmicpc.net/problem/2447
def printStar(N: int):
    if N==1:
        return ['*']
    nextStar = printStar(N//3)
    stars = []
    
    for star in nextStar:
        stars.append(star*3)
    for star in nextStar:
        stars.append(star+" "*(N//3)+star)
    for star in nextStar:
        stars.append(star*3)
    
    return stars
    
print("\n".join(printStar(int(input()))))

'''

# 숏코딩 https://www.acmicpc.net/source/43602819

N=int(input())
S='*'
while N>1:k=[c*3 for c in S];S=k+[c+' '*len(c)+c for c in S]+k;N//=3
print('\n'.join(S))

'''