import sys

n = int(sys.stdin.readline())
box = list(map(int,sys.stdin.readline().split()))
d = [0] * n 
for i in range(n):
    maximum = 0
    for j in range(i):
        if box[j] < box[i] and maximum < d[j]:
            maximum = d[j]
    d[i] = maximum + 1
print(max(d))
