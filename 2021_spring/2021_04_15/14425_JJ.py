import sys

input = sys.stdin.readline

n,m = map(int,input().split())

# 딕션너리 생성
strDict = {}

# 딕션너리 등록(해시)
for _ in range(n):
  tmp = input().rstrip()
  strDict[tmp] = True

ans = 0 

for _ in range(m):
  tmp = input().rstrip()
  # 등록되어 있으면 1증가
  if tmp in strDict:
    ans = ans + 1

print(ans)