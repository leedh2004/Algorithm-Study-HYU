import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
L = list(map(int,input().strip().split()))
cut = int(input().strip())
tree = {i: {j:0 for j in range(N)} for i in range(N)}
start = -1
result = 0

for child, parent in enumerate(L): #트리 만들기
    if parent == -1 :
        tree[parent] = {child : 1}
        continue
    tree[parent][child] = 1

for node in tree :
    tree[node][cut] = 0

# visit = [False for _ in range(N)]
q = deque()
q.append(-1)

while q :
    t = q.popleft()
    flag = True
    for k in tree[t]:
        if tree[t][k] == 1 :
            q.append(k)
            # visit[k] = True
            flag = False
    if flag and t != -1 :
        result += 1

print(result)