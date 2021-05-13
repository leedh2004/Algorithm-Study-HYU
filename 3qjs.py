from heapq import heappush, heappop


def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    tmp = [i for i in range(n)]
    deleted = []
    cur = k

    for c in cmd:
        if c[0] == 'U':
            _, idx = c.split()
            cur = tmp[cur-int(idx)]

        elif c[0] == 'D':
            _, idx = c.split()
            cur = tmp[cur+int(idx)]
        else:
            if c == "C":
                deleted.append(tmp[cur])
                popped = tmp.pop(cur)
                if tmp[-1] < popped:
                    cur = len(tmp)-1
            else:
                heappush(tmp, deleted.pop())
                # answer[restore] = 'O'
        # print(answer)

    print(tmp)
    print(deleted)
    return "".join(answer)
