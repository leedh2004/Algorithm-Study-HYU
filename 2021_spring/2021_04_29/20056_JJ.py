import sys
input = sys.stdin.readline

def move():
  newTable = [ [[] for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(len(table[i][j])):
        s = table[i][j][k][1]
        d = table[i][j][k][2]

        nx = i+dx[d]*s 
        ny = j+dy[d]*s 

        # 1번과 n번은 연결돠어 있음
        nx = (nx+n) % n
        ny = (ny+n) % n
        
        # d 방향으로 이동
        newTable[nx][ny].append(table[i][j][k][:])
  return newTable

def afterMove():
  for i in range(n):
    for j in range(n):

      # 2개 이하일때 continue
      if len(table[i][j]) < 2:
        continue

      m_sum = 0
      s_sum = 0
      allodd = True
      alleven = True
      for k in range(len(table[i][j])):
        m,s,d = table[i][j][k]
        m_sum = m_sum + m
        s_sum = s_sum + s
        if d%2 == 0:
          allodd = False
        else :
          alleven = False
      
      new_m = m_sum//5
      new_s = s_sum//len(table[i][j])

      # 질량 0인 경우
      if new_m == 0:
        table[i][j].clear()
        continue

      table[i][j] = [ [new_m,new_s, i*2 if (allodd or alleven) else i*2+1] for i in range(4) ]


def sumTable():
  ret = 0
  for i in range(n):
    for j in range(n):
      for k in range(len(table[i][j])):
        ret = ret + table[i][j][k][0]
  return ret

def printTable():
  for i in range(n):
    for j in range(n):
      print(table[i][j],end='')
      print('\t\t',end='')
    print('')
  print('')

n,m,k = map(int,input().split())

table = [ [[] for _ in range(n)] for _ in range(n)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for i in range(m):
  r, c, m, s, d = map(int,input().split())
  # 질량, 방향, 속력 저장
  table[r-1][c-1].append([m,s,d])

for i in range(k):
  # printTable()

  # 파이어볼 이동
  table = move()

  # 이동한 뒤, 파이어볼 2개 이상 있는 칸 처리
  afterMove()
# printTable()
print(sumTable()) 