import sys

def inRange(i,j):
    return ((0 <= i) and (i < N) and (0 <= j) and (j < N))
def crosscheck(i,j):
    idx = 0
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]
    x = i
    y = j
    #왼쪽 위
    while idx <= 3:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if inRange(nx,ny):
            if board[nx][ny] == 1: check[nx][ny] = True
        else:
            idx += 1
            x = i
            y = j
            continue
        x = nx
        y = ny
def reverseCrossCheck(i,j):
    idx = 0
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]
    x = i
    y = j
    while idx <= 3:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if inRange(nx,ny): 
            if board[nx][ny] == 1: check[nx][ny] = False
        else:
            idx += 1
            x = i
            y = j
            continue
        x = nx
        y = ny

def dfs(check,m_idx,cnt):
    if m_idx == M-1:
        return cnt

    ans = 0
    for i in range(M):
        cur_x,cur_y = starts[i]
        while inRange(cur_x,cur_y):
            if board[cur_x][cur_y] == 1 and not check[cur_x][cur_y]:
                check[cur_x][cur_y] = True
                crosscheck(cur_x,cur_y)
                ans = max(ans,dfs(check,m_idx+1,cnt+1))
                reverseCrossCheck(cur_x,cur_y)
                check[cur_x][cur_y] = False
            cur_x += 1
            cur_y += 1
    return ans


sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
board = [[] for _ in range(N)]
#True -> 갈 수 없다 False -> 아직 갈 수 있다.
check = [[False]* N for _ in range(N)]
bishops = [0] * (N*N)
for i in range(N):
    board[i] = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        if board[i][j] == 0: check[i][j] = True
#대각선으로 체크해줘야하는 줄 수 
M = (2 * N) -1
starts = []
for i in range(M):
    if i < N:
        starts.append([N-i-1,0])
    else:
        starts.append([0,i-N+1])
#왼쪽 아래 -> 오른 쪽 위로 줄선택순서
#해당 줄에서는 왼쪽 위부터 오른쪽 아래로 훑을 것
#print(check)
print(dfs(check,0,0))

"""
import sys

def inRange(i,j):
    return ((0 <= i) and (i < N) and (0 <= j) and (j < N))
def crosscheck(i,j):
    idx = 0
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]
    x = i
    y = j
    #왼쪽 위
    while idx <= 3:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if inRange(nx,ny):
            if board[nx][ny] == 1: check[nx][ny] = True
        else:
            idx += 1
            x = i
            y = j
            continue
        x = nx
        y = ny
def reverseCrossCheck(i,j):
    idx = 0
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]
    x = i
    y = j
    while idx <= 3:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if inRange(nx,ny): 
            if board[nx][ny] == 1: check[nx][ny] = False
        else:
            idx += 1
            x = i
            y = j
            continue
        x = nx
        y = ny

def dfs(check,m_idx,cnt):
    if m_idx == M:
        return cnt

    ans = 0
    for i in range(m_idx,M):
        cur_x,cur_y = starts[i]
        while inRange(cur_x,cur_y):
            if board[cur_x][cur_y] == 1 and not check[cur_x][cur_y]:
                check[cur_x][cur_y] = True
                #crosscheck(cur_x,cur_y)
                ans = max(ans,dfs(check,m_idx+1,cnt+1))
                #reverseCrossCheck(cur_x,cur_y)
                check[cur_x][cur_y] = False
            cur_x += 1
            cur_y += 1
    return ans


sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
board = [[] for _ in range(N)]
#True -> 갈 수 없다 False -> 아직 갈 수 있다.
check = [[False]* N for _ in range(N)]
bishops = []
for i in range(N):
    board[i] = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        if board[i][j] == 0: check[i][j] = True
#대각선으로 체크해줘야하는 줄 수 
M = (2 * N) -1
starts = []
for i in range(M):
    if i < N:
        starts.append([N-i-1,0])
    else:
        starts.append([0,i-N+1])
#왼쪽 아래 -> 오른 쪽 위로 줄선택순서
#해당 줄에서는 왼쪽 위부터 오른쪽 아래로 훑을 것
#print(check)
print(dfs(check,0,0))
"""