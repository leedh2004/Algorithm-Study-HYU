from bisect import bisect_left

d = {}

def solution(info, query):
    answer = []
    
    for idx in range(len(info)):
        i = info[idx].split()
        dfs('',i,0)
    
    for key in d:
        d[key] = sorted(d[key])
        
    for idx in range(len(query)):
        i = query[idx].split(' and ')
        tmp = i[3].split()
        i[3] = tmp[0]
        val = int(tmp[1])
        q = "".join(i)
        if q in d:
            answer.append(len(d[q]) - bisect_left(d[q],val))
        else :
            answer.append(0)
        
    return answer

def dfs(key,info,cnt):
    if cnt == 4:
        if not key in d:
            d[key] = []
        d[key].append(int(info[4]))
    else :
        dfs(key+'-',info,cnt+1)
        dfs(key+info[cnt],info,cnt+1)