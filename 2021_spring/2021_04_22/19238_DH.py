from collections import deque
import sys
import copy 
N, M, K = map(int, input().split())
board = []
for _ in range(N):
    t = list(map(int, input().split()))
    board.append(t)
# 택시
ty, tx = map(lambda x: int(x)-1, input().split())

#도착지
end = [ [ [] for _ in range(N) ] for _ in range(N) ]
for i in range(M):
    sy, sx, ey, ex = map(lambda x: int(x)-1, input().split())
    board[sy][sx] = i + 2
    end[ey][ex].append(i+2)

D = [(0, -1), (-1, 0), (0, 1), (1, 0)]

# for i in range(N):
#     for j in range(N):
#         print(board[i][j], end=' ')
#     print()

for i in range(M):
    # 손님을 태우러 감.
    q = deque()
    q.append((ty, tx, 0))
    dist = 10987654321
    visited = [[False]*N for _ in range(N)]
    visited[ty][tx] = True
    flag = False
    while q:
        y, x, d = q.popleft()
        # 연료보다 크다면 도달 못함.
        if d > K:
            break
        # 사람에게 도달했을 경우 거리가 같은 경우 행과 열이 작은것으로 선택함. 
        if board[y][x] > 1:
            flag = True
            if d > dist:
                break
            elif d == dist:
                if ty == y:
                    if x < tx:
                        ty, tx = y, x 
                elif y < ty:
                    ty, tx = y, x
            else:
                ty, tx = y, x
                dist = d
                K -= d 
        for i in range(4):
            ny, nx = y + D[i][0], x + D[i][1]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, d+1))
    if not flag:
        print("-1")
        sys.exit(0)
    # print("손님 탑승", ty, tx)
    # 도착지의 값
    nxt = board[ty][tx]
    board[ty][tx] = 0
    q = deque()
    q.append((ty, tx, 0))
    visited = [[False]*N for _ in range(N)]
    visited[ty][tx] = True
    flag = False
    while q:
        y, x, d = q.popleft()
        # 연료보다 크다면 도달 못함.
        if d > K:
            print("-1")
            sys.exit(0)
        # 목적지에 도달한 경우 연료 증가
        if len(end[y][x]) > 0:
            for val in end[y][x]:
                if val == nxt:
                    ty, tx = y, x
                    K += d
                    flag = True
                    break
        if flag:
            break
        for i in range(4):
            ny, nx = y + D[i][0], x + D[i][1]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, d+1))
    # print("손님 도착", ty, tx)
print(K)
        
        
        
    