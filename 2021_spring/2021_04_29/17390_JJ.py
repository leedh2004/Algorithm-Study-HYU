import sys

input = sys.stdin.readline

n,q = map(int,input().split())
arr = sorted( list(map(int,input().split())) )
acc = [ 0 for _ in range(n)]
tmp = 0

for i in range(n):
  tmp = tmp + arr[i]
  acc[i] = tmp

for j in range(q):
  st,ed = map(int,input().split())
  if st-2 < 0 :
    print(acc[ed-1])
  else :
    print(acc[ed-1]-acc[st-2])