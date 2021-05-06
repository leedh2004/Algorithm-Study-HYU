from collections import defaultdict
from bisect import bisect_left
def solution(info, query):
    answer = []
    d = defaultdict(lambda: [])
    def dfs(cnt, q, key):
        if cnt == 4:
            d[key].append(int(q[4]))
            return
        dfs(cnt+1, q, key+'-')
        dfs(cnt+1, q, key+q[cnt])
    for i in info:
        i = i.split()
        dfs(0, i, '')
    for key in d.keys():
        d[key] = sorted(d[key])
    for q in query:
        q = q.split(' and ')
        food, score = q[-1].split(' ')
        q = "".join(q[:-1] + [food])
        answer.append(len(d[q]) - bisect_left(d[q], int(score)))
    return answer