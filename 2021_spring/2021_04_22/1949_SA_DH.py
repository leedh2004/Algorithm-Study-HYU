from collections import deque
import copy 
T = int(input())
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(y, x, K, k_use):
    ret = 1
    find_max = 0
    for i in range(4):
        ny, nx = y + D[i][0], x + D[i][1]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            if board[ny][nx] < board[y][x]:
                visited[ny][nx] = 1
                find_max = max(find_max, dfs(ny, nx, K, k_use))
                visited[ny][nx] = 0
            elif board[ny][nx] - K < board[y][x] and not k_use:
                visited[ny][nx] = 1
                board[ny][nx] -= K
                find_max = max(find_max, dfs(ny, nx, K, True))
                board[ny][nx] += K
                visited[ny][nx] = 0
    ret += find_max
    return ret

for test_case in range(T):
    N, K = map(int, input().split())
    board = [] 
    for _ in range(N):
        t = list(map(int, input().split()))
        board.append(t)
    
    # 시작점 정보를 담는다.
    max_h = 0
    starts = [] 
    for y in range(N):
        for x in range(N):
            if board[y][x] > max_h:
                starts = [(y, x)]
                max_h = board[y][x]
            elif board[y][x] == max_h:
                
                starts.append((y, x))
    
    ans = 0
    # 시작점에서 DFS로 순회한다.
    for sy, sx in starts:
        q = deque()
        visited = [ [False]*N for _ in range(N) ]
        # K_를 사용했는지, K를 여기서 사용했는지
        ans = max(ans, dfs(sy, sx, K, False))
    print(ans)

