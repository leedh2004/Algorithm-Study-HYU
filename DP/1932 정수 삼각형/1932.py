
size = int(input())

d = [list(map(int, input().split())) for _ in range(size)]
maximum = 0
for i in range(1,size):
    for j in range(i+1):
        if(j==0):
            d[i][j] +=d[i-1][j]
        elif(j==i):
            d[i][i] += d[i-1][i-1]
        else:
            d[i][j] += max(d[i-1][j-1],d[i-1][j])
        if(maximum < d[i][j]):
            maximum = d[i][j]
print(maximum)
