import sys

N = int(sys.stdin.readline())
times = [0 for _ in range(N+1)]
tmp = [0 for _ in range(N+1)]
indegrees = [0 for _ in range(N+1)]
adj_list = dict()
for i in range(1, N+1):
    adj_list[i] = []
for i in range(1, N+1):
    info = list(map(int, sys.stdin.readline().split()))
    times[i] = info[0]
    tmp[i] = info[0]
    if info[1] != 0:
        for j in range(info[1]):
            adj_list[i].append(info[j+2])
            indegrees[info[j+2]] += 1

q = []
for i in range(1, N+1):
    if indegrees[i] == 0:
        q.append(i)

while q:
    cur = q.pop(0)

    for i in range(len(adj_list[cur])):
        next = adj_list[cur][i]
        if times[next] < tmp[next] + times[cur]:
            times[next] = tmp[next] + times[cur]

        indegrees[adj_list[cur][i]] -= 1
        if indegrees[adj_list[cur][i]] == 0:
            q.append(adj_list[cur][i])

print(max(times))
