import sys

T = int(sys.stdin.readline())
d = [[1,0],[0,1]]
for i in range(2,41):
    d.append([d[i-1][0]+d[i-2][0],d[i-1][1]+d[i-2][1]])
            
for i in range(T):
    a,b = d[int(sys.stdin.readline())]
    print(a,b)
