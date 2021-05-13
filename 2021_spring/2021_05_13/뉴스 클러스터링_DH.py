def solution(str1, str2):
    answer = 0
    set1 = [ str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha() ]
    set2 = [ str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha() ]
    
    s1 = set(set1)
    s2 = set(set2)
    
    union = s1 | s2
    intersection = s1 & s2
    u = 0 # union
    i = 0 # intersection
    
    for key in union:
        u += max(set1.count(key), set2.count(key))
    for key in intersection:
        i += min(set1.count(key), set2.count(key))

    if u == 0: return 65536
    return int(i / u * 65536)