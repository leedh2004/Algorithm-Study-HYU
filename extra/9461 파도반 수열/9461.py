import sys

T = int(sys.stdin.readline())
N=[]
append = N.append
for i in range(T):
    append(int(sys.stdin.readline()))
d = [0]*101
d[1] =1
d[2] =1
d[3] = 1
d[4] = 2
d[5] = 2
start = time.time()
maximum = N[0]
for num in N[1:]:
    if num > maximum:
        maximum = num

for i in range(6,maximum+1):
    d[i] = d[i-1]+d[i-5]

for i in range(T):
    print(d[N[i]])

