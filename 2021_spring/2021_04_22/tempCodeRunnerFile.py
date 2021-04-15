import copy
N, M, H = map(int, input().split())

def chk(b):
    global N, H
    for x in range(1, N+1):
        tmp = x
        for y in range(1, H+1): 
            if b[y][tmp] == 1:
                tmp += 1
            elif b[y][tmp-1] == 1:
                tmp -= 1
        if tmp != x:
            return False
    return True

def dfs(b, cnt, Y):
    global N, M, ans
    if cnt > 3 or ans <= cnt:
        return
    if chk(b):
        ans = min(ans, cnt)
        return
    for y in range(Y,H+1):
        for x in range(1, N):
            if b[y][x-1] == 0 and b[y][x+1] == 0 and b[y][x] ==0:
                b[y][x] = 1
                dfs(b, cnt+1, y)
                b[y][x] = 0

a = [ [0 for _ in range(N+1)] ] * (H+1)
for _ in range(M):
    A, B = map(int, input().split())
    a[A][B] = 1
ans = 987654321
dfs(a, 0, 0)
print(ans if ans < 4 else -1)