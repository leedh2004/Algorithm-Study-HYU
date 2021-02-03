import sys

# roll = 1~20 / devil,angel = 1 ~ 100 길이 같다
roll = sys.stdin.readline().rstrip()  
devil = sys.stdin.readline().rstrip()
angel = sys.stdin.readline().rstrip()
l = len(devil)

# len(roll) * len(devil) * 2  ([0]-devil 끝,[1]-angel 끝)
d = [[[0 for d in range(2)] for a in range(l)] for _ in range(len(roll))]

for i in range(l):
    if devil[i] == roll[0]:
        d[0][i][0] = 1
    if angel[i] == roll[0]:
        d[0][i][1] = 1

for i in range(len(roll)-1): # i+1연산 때문에 
    for j in range(len(devil)):
        if roll[i] == devil[j]:
            for k in range(j+1,l):
                if roll[i+1] == angel[k]:
                    d[i+1][k][1] += d[i][j][0]
        if roll[i] == angel[j]:
            for k in range(j+1,l):
                if roll[i+1] == devil[k]:
                    d[i+1][k][0] += d[i][j][1]
# print(d)
ans = 0
for i in range(l):
    ans += sum(d[-1][i])

print(ans)
            