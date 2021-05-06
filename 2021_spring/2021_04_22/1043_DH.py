import sys

def get_parent(a):
    global P
    if P[a] == a:
        return a
    else:
        parent = get_parent(P[a])
        P[a] = parent
        return P[a]

def union(a, b):
    global P
    pa = get_parent(a)
    pb = get_parent(b)
    if pb > pa:
        P[pa] = pb
    else:
        P[pb] = pa

N, M = map(int, input().split())
P = [ i for i in range(N+1) ]
# True Know People
T_P = list(map(int, input().split()))[1:]
if len(T_P) == 0:
    print(M)
    sys.exit(0)
else:
    for i in range(len(T_P)-1):
        union(T_P[i], T_P[i+1])

ans = 0
T = []
for _ in range(M):
    People = list(map(int, input().split()))[1:]
    T.append(People)
    len_p = len(People)
    for i in range(len_p-1):
        union(People[i], People[i+1])

for People in T:
    flag = True 
    for p in People:
        if get_parent(p) == get_parent(T_P[0]):
            flag = False
            break
    if flag:
        ans += 1

print(ans) 

