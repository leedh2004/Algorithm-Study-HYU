import sys

input = sys.stdin.readline

n = int(input())
goaltmp = list(map(int,input().split()))

# boolean 으로 변환
goal = []
for i in range(n):
  if goaltmp[i] == 0:
    goal.append(False)
  else : 
    goal.append(True)

now = [False for _ in range(n)]
ans = 0

for i in range(n):
  # 목표하는바와 다를때
  if now[i]!= goal[i]:
    now[i] = not now[i]

    # 범위 체크
    if i + 1 < n :
      now[i+1] = not now[i+1]
      
    # 범위 체크
    if i + 2 < n :
      now[i+2] = not now[i+2]
    ans = ans + 1

print(ans)

