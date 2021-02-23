import sys

# Test case
t = int(sys.stdin.readline())

for k in range(t):
  n = int(sys.stdin.readline())
  bRank = list(map(int,sys.stdin.readline().split()))
  idxRank = [0 for _ in range(n)]
  data = []
  for i in range(len(bRank)):
    # [팀 인덱스,등수]
    data.append([bRank[i],i])

    # 등수를 인덱스순으로 저장
    idxRank[bRank[i]-1] = i
  
  # 팀 인덱스 순으로 정렬
  data.sort()

  m = int(sys.stdin.readline())
  for i in range(m):
    a,b = map(int,sys.stdin.readline().split())

    # b가 등수가 더 높을때(숫자가 작을때)
    if idxRank[a-1] > idxRank[b-1]:
      data[b-1][1] =  data[b-1][1] + 1
      data[a-1][1] =  data[a-1][1] - 1
    else :
      data[a-1][1] =  data[a-1][1] + 1
      data[b-1][1] =  data[b-1][1] - 1
    
  data.sort(key=lambda x:(x[1]))

  # 일관성 없는 경우 조사
  cnt = 0
  flag = True
  for i in range(n):
    if i!=data[i][1]:
      flag = False
      break
  
  if not flag:
    print("IMPOSSIBLE")
  else :
    for i in range(n):
      print(data[i][0],end=" ")


  