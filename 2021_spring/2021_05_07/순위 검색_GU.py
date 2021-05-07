def solution(info, query):
    answer = []
    cpps, javas, pythons = [], [], []
    for i in range(len(info)):
        info[i] = info[i].split()
        if info[i][0][0] == 'c':
            cpps.append(info[i])
        elif info[i][0][0] == 'j':
            javas.append(info[i])
        else:
            pythons.append(info[i])

    for i in range(len(query)):
        q = query[i]
        q = q.split()
        X = int(q[-1])
        if q[0] == '-':
            candidate = info[:]
            cnt = len(info)
        elif q[0] == 'cpp':
            candidate = cpps[:]
            cnt = len(cpps)
        elif q[0] == 'java':
            candidate = javas[:]
            cnt = len(javas)
        else:
            candidate = pythons[:]
            cnt = len(pythons)

        for j in candidate[:]:
            if int(j[-1]) < X:
                candidate.remove(j)
                cnt -= 1
        if cnt == 0:
            answer.append(0)
            continue
        a, b, c, d = q[0], q[2], q[4], q[6]

        for j in range(len(candidate)):
            if a != '-':
                if candidate[j][0] != a:
                    cnt -= 1
                    continue
            if b != '-':
                if candidate[j][1] != b:
                    cnt -= 1
                    continue
            if c != '-':
                if candidate[j][2] != c:
                    cnt -= 1
                    continue
            if d != '-':
                if candidate[j][3] != d:
                    cnt -= 1
        answer.append(cnt)
    return answer
