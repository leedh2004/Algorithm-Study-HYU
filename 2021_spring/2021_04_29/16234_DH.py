import sys
from collections import defaultdict

N, L, R = map(int, sys.stdin.readline().strip().split())
b = []

for _ in range(N):
    t = list(map(int, sys.stdin.readline().strip().split()))
    b.append(t)

D = [(0,1), (0,-1), (1, 0), (-1,0)]

def dfs(y, x, cnt, flag, dict, visited):
    global L, R, b, D
    if visited[y][x] != 0:
        return False
    visited[y][x] = cnt
    dict[cnt] = (dict[cnt][0] + b[y][x], dict[cnt][1] + 1)
    for i in range(4):
        ny, nx = y + D[i][0], x + D[i][1]
        if 0 <= ny < N and 0 <= nx < N:
            if L <= abs(b[y][x] - b[ny][nx]) <= R:
                flag = True
                dfs(ny, nx, cnt, flag, dict, visited)
    return flag

ans = 0

while True:
    visited = [ [0] * N for _ in range(N) ]
    cnt = 1
    flag = False
    dd = defaultdict(lambda: (0, 0))
    for y in range(N):
        for x in range(N):
            cnt += 1
            if dfs(y, x, cnt, False, dd, visited):
                flag = True 
    
    if flag == False:
        break
    else:
        ans += 1

    for y in range(N):
        for x in range(N):
            key = visited[y][x]
            s, cnt = dd[key][0], dd[key][1]
            b[y][x] = int(s / cnt)

print(ans)
            
