import sys

# 입력
n = int(sys.stdin.readline())
lines = []
for i in range(n):
  st,ed = map(int,sys.stdin.readline().split())
  lines.append([st,ed])

# 정렬
lines.sort()

ans = 0
left,right = -1000000001,-1000000001
# 스위핑 알고리즘
for i in range(n):
  # 이어지는 경우
  if right >= lines[i][0]:
    right = max(right,lines[i][1])
  
  # 새로운 구간
  else : 
    ans = ans + right-left
    left = lines[i][0]
    right = lines[i][1]

# 마지막 구간 고려
ans = ans + right-left
print(ans)