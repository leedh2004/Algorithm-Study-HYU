import sys
import bisect
from collections import deque

imput = sys.stdin.readline

def gcd(a,b):
  if b==0 :
    return a
  return gcd(b,a%b)

def solve():

  m = int(input())
  allgcd = 0
  
  moneys = []
  lefts = []
  beforeLeft = 0

  for i in range(m):
    money,left = map(int,input().split())

    # 데이터 저장
    moneys.append(money)
    lefts.append(left)

    # 출금일 때
    if money < 0 :
      chargedMoney = left - money - beforeLeft
    
      # 실제 충전이 되었을 때
      if chargedMoney > 0:
        allgcd = gcd(chargedMoney,allgcd)

    beforeLeft = left

  if allgcd == 0:
    allgcd = 1

  beforeLeft = 0
  for i in range(m):

    # 입금일때
    if moneys[i] >= 0:

      # 일치하지 않는다면
      if beforeLeft + moneys[i] != lefts[i]:
        return -1

    # 출금일때 
    else :
      
      # 충전이 필요없을 때
      if -moneys[i] <= beforeLeft :

        # 일치하지 않는다면
        if beforeLeft + moneys[i] != lefts[i]:
          return -1

      # 충전 필요할 때
      else :
        if allgcd <= lefts[i]:
          return -1

    beforeLeft = lefts[i]

  return allgcd

print(solve())
  
  
# def sliceList(arr,val):
#   idx = bisect.bisect_right(arr,val)
#   if len(arr) == idx:
#     return []
#   else :
#     return arr[idx:]

# def solve():
#   m = int(input())
#   data = []
#   beforeLeft = 0
#   for i in range(m):
#     money,left = map(int,input().split())
#     # 출금일 때
#     if money < 0 :
#       chargedMoney = left - money -beforeLeft

#       # 실제 충전이 되었을 때
#       if chargedMoney > 0:

#         # 가능한 약수 목록
#         tmpArr = get_list(chargedMoney)
#         tmpArr2 = sliceList(tmpArr,left)
#         tmpDict = {num : True for num in tmpArr2}
#         data.append(tmpDict)
      
#     beforeLeft = left

#   # 후보가 적은 순으로 정렬
#   data = sorted(data, key= lambda x: len(x))
#   # print(data)
#   ansDict = data[0]

#   for i in range(1,len(data)):
#     newAnsList = {}
#     for ans in ansDict:
#       if ans in data[i]:
#         newAnsList[ans] = True
    
#     # 공통된 공약수 후보가 없을 때
#     if len(newAnsList) == 0: 
#       return -1

#     ansDict = newAnsList
  
#   for ans in ansDict:
#     return ans

# print(sliceList([1,2,3],4))


