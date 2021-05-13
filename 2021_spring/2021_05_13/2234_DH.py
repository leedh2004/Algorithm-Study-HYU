N, M = map(int, input().split())
B = [ list(map(int, input().split())) for _ in range(M) ]
D = [(0, -1), (-1, 0), (0, 1), (1, 0)]
visited = [ [ 0 for _ in range(N) ]for _ in range(M) ]
R = {}
def dfs(y, x, number):
    global visited, N, M, B
    if visited[y][x] != 0:
        return 0
    ret = 1
    visited[y][x] = number
    val = B[y][x]
    for dy, dx in D:
        ny, nx = y + dy, x + dx
        if 0 <= ny < M and 0 <= nx < N and visited[ny][nx] == 0 and val & 1 == 0:
            ret += dfs(ny, nx, number)
        val = val >> 1
    return ret

room_number = 0
max_v = 0
max_sum_v = 0
R = {} 

for y in range(M):
    for x in range(N):
        if visited[y][x] == 0:
            room_number += 1
            v = dfs(y, x, room_number)
            R[room_number] = v
            max_v = max(v, max_v)
visited2 = [ [ False for _ in range(N) ]for _ in range(M) ]
def dfs2(y, x):
    global visited, visited2, N, M, B, max_sum_v, R
    if visited2[y][x] == True:
        return
    visited2[y][x] = True
    for dy, dx in D:
        ny, nx = y + dy, x + dx
        if 0 <= ny < M and 0 <= nx < N:
            # 서로 다른 방임
            if visited[y][x] != visited[ny][nx]:
                ret = R[visited[y][x]] + R[visited[ny][nx]]
                max_sum_v = max(max_sum_v, ret)
            else:
                dfs2(ny, nx)
    return

for y in range(M):
    for x in range(N):
        if visited2[y][x] == 0:
            dfs2(y, x)
print(room_number)
print(max_v)
print(max_sum_v)