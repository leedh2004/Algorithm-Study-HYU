import sys

change = [500,100,50,10,5,1]

n = 1000 - int(sys.stdin.readline())
res =0
for i in range(6):
    res += (n//change[i])
    n %= change[i]
print(res)