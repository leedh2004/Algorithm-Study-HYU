import sys
import bisect

# 입력
n,m = map(int,sys.stdin.readline().split())
names, powers = [],[] 
for i in range(n):
  name,power = sys.stdin.readline().rstrip().split()
  names.append(name)
  powers.append(int(power))

for i in range(m):
  p = int(sys.stdin.readline())
  # 이분탐색
  idx = bisect.bisect_left(powers,p)
  print(names[idx])
