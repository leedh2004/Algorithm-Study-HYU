import sys

input = sys.stdin.readline


def solve():
  rotate_table = [[table[x][y] for x in range(n)] for y in range(n)]
  ans = checkTable(table) + checkTable(rotate_table)
  return ans

def checkTable(Table):
  count = 0
  for row in Table:
    if checkRow(row):
      count=count+1
  return count

def checkRow(Row):
  flag = True 
  check = [False for _ in range(n)] # 경사로 놓여있는 지점 체크
  for i in range(n-1):

    # 더 작은 경우
    if Row[i] < Row[i+1]:
      
      # 좁아서 경사로 못 놓음
      if i+1<l:
         flag=False
      else :
        for j in range(l):
          if Row[i+1]-1 != Row[i-j] or check[i-j]:
            flag = False 
          check[i-j] = True
    
    # 더 큰 경우
    elif Row[i] > Row[i+1]:

      # 좁아서 경사로 못 놓음
      if i+l >= n:
        flag=False

      else :
    
        for j in range(l):
          
          if Row[i]-1 != Row[i+1+j] or check[i+1+j]:
            flag = False
          check[i+j+1] = True

  return flag

n,l = map(int,input().split())

table = []
for i in range(n):
  table.append(list(map(int,input().split())))

print(solve())
