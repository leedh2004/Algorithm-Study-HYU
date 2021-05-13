import sys

input = sys.stdin.readline

n,q = map(int,input().split())
# 오름차순 정렬
arr = sorted( list(map(int,input().split())) )
acc = [ 0 for _ in range(n)]
tmp = 0

# 누적합 배열 생성
for i in range(n):
  tmp = tmp + arr[i]
  acc[i] = tmp


for j in range(q):
  st,ed = map(int,input().split())
  st,ed = st-1 ,ed-1
  if st == 0 :
    print(acc[ed])
  else :
    # 구간합
    print(acc[ed]-acc[st-1])