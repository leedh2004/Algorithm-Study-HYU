import sys

input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())
table = []

for i in range(n):
  tmp =  list(map(int,input().split()))
  table.append(tmp)

# 위, 아래, 동, 서, 남, 북
dice = [0,0,0,0,0,0]

def move(nowdice,val):
  nextdice = None

  if val == 1:
    nextdice = [nowdice[3],nowdice[2],nowdice[0],nowdice[1],nowdice[4], nowdice[5]]
  elif val==2:
    nextdice = [nowdice[2],nowdice[3],nowdice[1],nowdice[0],nowdice[4], nowdice[5]]
  elif val==3:
    nextdice = [nowdice[4],nowdice[5],nowdice[2],nowdice[3],nowdice[1], nowdice[0]]
  else :
    nextdice = [nowdice[5],nowdice[4],nowdice[2],nowdice[3],nowdice[0], nowdice[1]]
  return nextdice

def is_in(a,b):
  return 0<=a<n and 0<=b<m

command = list(map(int,input().split()))
nowx,nowy = x,y
d = [[0,1],[0,-1],[-1,0],[1,0]]
for val in command:
  nextx,nexty = nowx+d[val-1][0],nowy+d[val-1][1]
  # 범위 확인
  if is_in(nextx,nexty):

    # 이동
    dice = move(dice,val)

    # 복사
    if table[nextx][nexty] == 0:
      table[nextx][nexty] = dice[1]
    else:
      dice[1] = table[nextx][nexty]
      table[nextx][nexty] = 0
    
    nowx,nowy = nextx,nexty

    print(dice[0]) # 윗면
   


