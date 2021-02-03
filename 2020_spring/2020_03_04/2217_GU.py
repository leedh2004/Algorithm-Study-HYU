import sys

n = int(sys.stdin.readline())
r = [0]*n
for i in range(n):
    r[i] = int(sys.stdin.readline())
r.sort()
maximum = 0

for i in range(n):
    w = r[i] * (n-i)
    if maximum < w:
        maximum = w

print(maximum)