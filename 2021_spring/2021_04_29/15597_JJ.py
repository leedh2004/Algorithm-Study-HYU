import sys

input = sys.stdin.readline

def getMaxData(point,maxVal):
  maxValList = []
  for i in range(len(point)):
    if point[i] == maxVal :
      maxValList.append(i)
  return maxValList

nameList = input().split()
nameIdx = {}
point = [0.0, 0.0, 0.0, 0.0]
for i in range(4):
  nameIdx[nameList[i]] = i

for j in range(6):
  tmp = input().split()
  idx1,idx2 = nameIdx[tmp[0]],nameIdx[tmp[1]]
  win,draw,loss = map(float,tmp[2:])
  point[idx1] = point[idx1] + win*3 + draw
  point[idx2] = point[idx2] + loss*3 + draw

# 가장 큰 녀석
maxVal1,maxVal1List = max(point),getMaxData(point, max(point))

ret = [0.0, 0.0, 0.0, 0.0]
# print(point)

# 2개 이상
if len(maxVal1List) > 1:
  for i in range(len(maxVal1List)):
    ret[maxVal1List[i]] = 2.0 / len(maxVal1List)

# 1개 일때 
else :
  ret[maxVal1List[0]] = 1.0
  
  # 2번째 큰 녀석
  maxVal2List = []
  maxVal2 = -1
  for i in range(4):
    if maxVal1 == point[i]:
      continue

    if maxVal2 < point[i]:
      maxVal2 = point[i]
      maxVal2List = [i]
    elif maxVal2 == point[i]:
      maxVal2List.append(i)

  if len(maxVal2List) > 1:
    for i in range(len(maxVal2List)):
      ret[maxVal2List[i]] = 1.0 / len(maxVal2List)
  else :
    ret[maxVal2List[0]] = 1.0

for i in range(4):
  print("%0.10f"%ret[i])







