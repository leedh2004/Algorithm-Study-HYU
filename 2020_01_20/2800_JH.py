from itertools import combinations

e = list(input())
p, p_idx = [], []
idx = 0

for i, c in enumerate(e):
    if c == '(' :
        p.append(i)
    if c == ')' :
        s = p.pop()
        p_idx.append([s,i])

result = set()

for i in range(1,len(p_idx)+1):
    for j in combinations(p_idx,i):
        tmp_result = e[:]
        for o,c in j :
            tmp_result[o], tmp_result[c] = '', ''
            
        result.add("".join(tmp_result))

for i in sorted(result):
    print(i)