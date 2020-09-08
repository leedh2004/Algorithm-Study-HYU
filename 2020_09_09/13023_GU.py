import sys

def dfs(s,check,cnt):
    # 4개 연결 -> 5명 친구
    if cnt == 4:
        print(1)
        #print 1 하고는 프로그램 종료...
        exit(0)
    for i in range(len(relation[s])):
        next_ = relation[s][i]
        if not check[next_]:
            check[next_] = True
            dfs(next_,check,cnt+1)
            check[next_] = False

N,M = map(int,sys.stdin.readline().split())
relation = [[] for _ in range(N)]
start = []
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)
    start.append(a)
    start.append(b)
start = list(set(start))

for s in start:
    check = [False] * N
    check[s] = True
    dfs(s,check,0)
print(0)


"""
import sys
sys.setrecursionlimit(2000)
def dfs(s,check,cnt):
    check[s] = True
    cnt+= 1
    cur = s

    all_checked = True
    for i in range(len(relation[cur])):
        next_ = relation[cur][i]
        if not check[next_]:
            all_checked = False
            return dfs(next_,check,cnt)
    if all_checked:
        return cnt


N,M = map(int,sys.stdin.readline().split())
relation = [[] for _ in range(N)]
start = []
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)
    start.append(a)
    start.append(b)
start = list(set(start))
print(relation)
#check = [False] * N
print(start)

ABCDE = False
for s in start:
    check = [False] * N
    if dfs(s,check,0) >=5:
        ABCDE = True
        print(1)
        break
if not ABCDE: print(0)
"""
