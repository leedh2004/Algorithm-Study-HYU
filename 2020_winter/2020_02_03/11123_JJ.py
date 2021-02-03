import sys

sys.setrecursionlimit(10**7)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def is_in(y,x):
  global r,c
  return  0 <= y and y < r and 0 <= x and x < c

def dfs(y,x):
  global visited,table,dx,dy

  # 방문 체크
  visited[y][x] = True

  # 4방향 조사
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    # 범위내이면서, 방문 안했고, 양이라면
    if is_in(ny,nx) and not visited[ny][nx] and table[ny][nx] == '#':
      dfs(ny,nx)



# 입력
t= int(sys.stdin.readline())
for k in range(t):
  r,c = map(int,sys.stdin.readline().split())
  table = []
  for i in range(r):
    table.append(sys.stdin.readline().rstrip())
  visited = [[False for _ in range(c)] for _ in range(r)]

  # 결과값
  ans = 0

  for i in range(r):
    for j in range(c):
      if not visited[i][j] and table[i][j] == '#' :
        dfs(i,j)
        ans = ans + 1

  print(ans)
