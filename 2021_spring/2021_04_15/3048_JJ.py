import sys
input = sys.stdin.readline


# 입력
n,m = map(int,input().split())
left = list(input().rstrip())
right = list(input().rstrip())
time = int(input())

# 전체 문자열
nowAnts =  [ [left[len(left)-idx-1],'L'] for idx in range(len(left)) ]  + [ [right[idx],'R'] for idx in range(len(right)) ]

for _ in range(time):

  nextAnts = nowAnts[:]
  flag = False
  for j in range(len(nowAnts)-1):
    # 서로 뛰어넘어야 하는 경우
    if nowAnts[j][1] == 'L' and nowAnts[j+1][1] == 'R':

      # 스왑
      nextAnts[j] = nowAnts[j+1][:]
      nextAnts[j+1] = nowAnts[j][:]

      flag = True

  if not flag:
    break

  nowAnts = nextAnts[:]

print("".join([ nowAnts[idx][0] for idx in range(len(nowAnts))] ))


