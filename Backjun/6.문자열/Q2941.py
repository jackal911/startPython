# 크로아티아 알파벳 https://www.acmicpc.net/problem/2941
string = input()
count = 0
i = 0
while i<len(string):
    if i==len(string)-1: # IndexError 때문
        count += 1
        i += 1
    elif string[i]=='c' and (string[i+1]=='=' or string[i+1]=='-'):
        count += 1
        i += 2
    elif string[i]=='d' and string[i+1]=='-':
        count += 1
        i += 2
    elif string[i]=='l' and string[i+1]=='j':
        count += 1
        i += 2
    elif string[i]=='n' and string[i+1]=='j':
        count += 1
        i += 2
    elif string[i]=='s' and string[i+1]=='=':
        count += 1
        i += 2
    elif string[i]=='z' and string[i+1]=='=':
        count += 1
        i += 2
    elif i==len(string)-2 and string[i]=='d': # IndexError 때문
        count += 1
        i += 1
    elif string[i]=='d' and string[i+1]=='z' and string[i+2]=='=':
        count += 1
        i += 3
    else:
        count += 1
        i += 1
print(count)

'''시도1

croas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = stringTemp = input()
count = 0
for croa in croas:
    if (inclu:=string.count(croa)) and stringTemp.count(croa):
        count += inclu
        stringTemp = stringTemp.replace(croa, "")
print(count+len(stringTemp))

# 반례 : string = 'cc=-c-'
# 정답 : 4
# 출력 : 2
'''

'''

import re
print(len(re.sub('dz=|[ln]j|\w\W','Z',input())))

'''