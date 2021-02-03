import sys

def inBorder(y,x):
    global N,M
    return ((y>=0)and(y<N)) and ((x>=0)and(x<M))

def check(y,x,sz):
    global map_
    cur = map_[y][x]
    if(cur == map_[y][x+sz-1] and cur == map_[y+sz-1][x] and cur ==map_[y+sz-1][x+sz-1]):
        return True
    else: return False
    

        

N,M = map(int,sys.stdin.readline().split())
map_ = [[0]*M for _ in range(N)]
ans = 0
for i in range(N):
    line = list(sys.stdin.readline())
    for j in range(M):
        map_[i][j] = int(line[j])

sz = min(N,M)
done = False
for k in range(sz,0,-1):
    if done:
        break
    for i in range(N-k+1):
        if done:
            break
        for j in range(M-k+1):
            if(inBorder(i+k-1,j+k-1)):
                if(check(i,j,k)):
                    ans = k*k
                    done = True
                    break
print(ans)
