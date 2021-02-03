import sys

input = sys.stdin.readline
N = int(input())
train = list(map(int,input().split()))
maximum = int(input())
combination = []
for i in range(N-maximum+1):
    tmp = 0
    for j in range(maximum):
        tmp += train[i+j]
    combination.append(tmp)
#print(combination)
d = [[0] * 3 for _ in range(N+1)]
#for i in range(N-maximum+1):
#    d[maximum+i][0] = combination[i]
d[maximum][0] = combination[0]
for i in range(maximum,N+1):
    for k in range(maximum,i-maximum+1):
        for j in range(2):
            d[i][j+1] = max(d[i-1][j+1],d[k][j]+combination[i-maximum])
print(d[N][2])
print(d)