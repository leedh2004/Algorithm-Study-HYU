def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    deleted = []
    cur = k

    for c in cmd:
        if len(c) > 1:
            _cmd, idx = c.split()
            idx = int(idx)
            cnt = 0
            if _cmd == 'U':
                for i in range(cur-1, -1, -1):
                    if answer[i] == 'O':
                        cnt += 1
                        if cnt == idx:
                            cur = i
                            break
            elif _cmd == 'D':
                for i in range(cur+1, n):
                    if answer[i] == 'O':
                        cnt += 1
                        if cnt == idx:
                            cur = i
                            break
        else:
            if c == "C":
                answer[cur] = 'X'
                deleted.append(cur)
                is_last = True
                for i in range(cur+1, n):
                    if answer[i] == 'O':
                        cur = i
                        is_last = False
                        break
                if is_last:
                    for i in range(cur-1, -1, -1):
                        if answer[i] == 'O':
                            cur = i
                            break
            else:
                restore = deleted.pop()
                answer[restore] = 'O'
        # print(answer)

    return "".join(answer)
