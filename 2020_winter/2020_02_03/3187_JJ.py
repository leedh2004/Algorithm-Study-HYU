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
  
  # 현재 위치 고려
  wolf, sheep = 0,0
  if table[y][x] == 'v':
    wolf = 1
  elif table[y][x] == 'k':
    sheep = 1

  # 4방향 조사
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    # 범위내이면서, 방문 안했고, 울타리로 막히지 않았다면
    if is_in(ny,nx) and not visited[ny][nx] and table[ny][nx] != '#':
      n_wolf,n_sheep =  dfs(ny,nx)
      wolf,sheep = wolf + n_wolf , sheep + n_sheep

  return wolf,sheep


# 입력
r,c = map(int,sys.stdin.readline().split())
table = []
for i in range(r):
  table.append(sys.stdin.readline().rstrip())
visited = [[False for _ in range(c)] for _ in range(r)]

# 결과값
wolfAns,sheepAns = 0,0

for i in range(r):
  for j in range(c):
    if not visited[i][j] and table[i][j] != '#' :
      wolf,sheep =  dfs(i,j)
      # 양이 다 잡아먹힘
      if wolf >= sheep :
        wolfAns = wolfAns + wolf
      # 늑대가 다 잡아먹힘
      else :
        sheepAns = sheepAns + sheep

print('%d %d'%(sheepAns,wolfAns))
