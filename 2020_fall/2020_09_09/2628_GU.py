import sys

w,h = map(int,sys.stdin.readline().split())
T = int(sys.stdin.readline())
garo = [0,w]
sero = [0,h]
for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    if a==0: sero.append(b)
    else: garo.append(b)
garo.sort()
sero.sort()
width = 0
height = 0
for i in range(1,len(garo)):
    width = max(width,garo[i]-garo[i-1])
for i in range(1,len(sero)):
    height = max(height,sero[i]-sero[i-1])
print(width*height)