def solution(str1, str2):
    answer = 0
    S1 = []
    for i, j in zip(str1, str1[1:]):
        if i.isalpha() and j.isalpha():
            S1.append(i.lower()+j.lower())
    S2 = []
    for i, j in zip(str2, str2[1:]):
        if i.isalpha() and j.isalpha():
            S2.append(i.lower()+j.lower())
    set1 = set(S1)
    set2 = set(S2)
    # intersect
    set3 = set1 & set2
    set4 = set1 | set2

    d1 = {i: 0 for i in set4}
    d2 = {i: 0 for i in set4}

    for i in range(len(S1)):
        d1[S1[i]] += 1
    for i in range(len(S2)):
        d2[S2[i]] += 1

    d3 = {i: 0 for i in set3}
    d4 = {i: 0 for i in set4}

    for i in set3:
        d3[i] = min(d1[i], d2[i])
    for i in set4:
        d4[i] = max(d1[i], d2[i])

    # sum(d3.values()) == 0 and 하니깐 틀림
    if sum(d4.values()) == 0:
        return 65536
    return int((sum(d3.values())/sum(d4.values())) * 65536)
