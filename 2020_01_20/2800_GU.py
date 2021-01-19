import sys
# import re
from itertools import combinations
from copy import deepcopy

# def replace_str_index(text,index=0,replacement=''):
#     return '%s%s%s'%(text[:index],replacement,text[index+1:])

sik = sys.stdin.readline().rstrip()
sik2 = deepcopy(sik)
parenthesis_cnt = sik.count('(')
parenthesis = []
stack = []

count = 0
for i in range(len(sik)):
    if sik[i] == '(':
        stack.append(i)
    elif sik[i] == ')':
        parenthesis.append([stack[-1],i])
        stack.pop(-1)
#print(parenthesis)

comb = []
for i in range(1,parenthesis_cnt+1):
    comb.extend(list(combinations(parenthesis,i)))
ans = []
for i in range(len(comb)):
    tmp = list(deepcopy(sik))
    for j in range(len(comb[i])):
        front,back = comb[i][j]
        tmp[front]= '$'
        tmp[back] = '$'
    #tmp = str(tmp)
    tmp2 = ''.join(tmp)
    #print(tmp2)
    #ans.append(re.sub('$','',str(tmp)))
    ans.append(str(tmp2.replace('$','')))

# 중복인 경우가 있다
ans = list(set(ans))
# 사전순
ans.sort()
for answer in ans:
    print(answer)