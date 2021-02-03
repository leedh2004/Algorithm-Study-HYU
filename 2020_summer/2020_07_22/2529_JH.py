#2529 - 부등호

import copy
def check(n,tmp,pre_digit):
    global K,max_result,min_result
    digit = copy.copy(pre_digit)

    if n == K :
        max_result = str(max(int(max_result),int(tmp)))
        min_result = str(min(int(min_result),int(tmp)))
        return

    if connect[port[n]-1] == True : #모르겠슴니당
        pass

    else :
        return

    for i in range(n+1,K+1,1):
        check(i,tmp,digit)


K = int(input())
sign = input().split()
digit = [True for _ in range(10)]
max_result = ""
min_result = ""

for i in range(10):
    check(i,"",digit)

print(max_result)
print(min_result)