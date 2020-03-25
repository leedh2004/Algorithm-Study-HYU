import sys
ret = 100000
#visit = [0] * 100000
def dfs(a,b,cnt):
    global ret
    if cnt >= ret:
        return
    if a == b:
        ret = cnt
        return
    if cnt >= direct:
        return
    if a < b:
        if a+1 < 100001:
            dfs(a+1,b,cnt+1)
        if 2*a < 100001:
            dfs(2*a,b,cnt+1)
    elif a-1 >= 0:
        dfs(a-1,b,cnt+1)
    
    
a,b = map(int,sys.stdin.readline().split())
direct = abs(a-b)
dfs(a,b,0)
if ret > direct:
    print(direct)
else:
    print(ret)
