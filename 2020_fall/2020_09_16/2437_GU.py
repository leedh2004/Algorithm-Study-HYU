import sys

# 추들을 sort하고 작은 것부터 하나씩 더한다.
# 수열이 연속성을 가질 때 하나의 추 더하고도 연속성 계속 있는지 확인
# 다음 추가 last +1 이하면 가능
input = sys.stdin.readline
N = int(input())
choo = list(map(int,input().split()))
if N == 1:
    if choo[0] != 1:
        print(1)
        exit(0)
    else:
        print(2)
        exit(0)
choo.sort()
first = choo[0]
# last = 1~ last까지 무게 가능
last = choo[0]+choo[1]
if first != 1:
    print(1)
    exit(0)
elif N==2:
    if choo[1] == 1:
        print(3)
    elif choo[1] ==2:
        print(4)
    else:
        print(2)
else:
    if choo[1] - choo[0] > 1:
        print(2)
    else:
        for i in range(2,N):
            next_ = choo[i]
            nfirst = 1 + next_
            nlast = last + next_
            # nfirst -> next_ 자기 자신도 들어가면서 연속성 완성가능
            if next_ <= last + 1: # 가능
                last = nlast
            else:
                break
#last가 지금까지 표현할 수 있는 최대 -> so +1
print(last+1)
    

# 시간 초과
"""def check(t,idx):
    for i in range(idx-1,-1,-1):
        if t < choo[i]: continue
        t -= choo[i]
        if t==0: return True
    return False

input = sys.stdin.readline
N = int(input())
choo = list(map(int,input().split()))
choo.sort()
max_ = sum(choo)
idx = 0
for i in range(1,max_+1):
    if i in choo: continue
    else:
        choo.append(i)
        choo.sort()
        idx = choo.index(i)
        if not check(i,idx): 
            print(i)
            break
        choo.pop(idx)"""