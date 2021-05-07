def is_right(p):
    tmp = []
    for i in range(len(p)):
        if p[i] == '(':
            tmp.append(p[i])
        elif p[i] == ')':
            if tmp:
                tmp.pop()
            else:
                return False
    return True


def _split(p):
    L = 0
    R = 0
    for i in range(len(p)):
        if p[i] == '(':
            L += 1

        elif p[i] == ')':
            R += 1

        if L == R:
            return i

    return len(p)-1


def solution(p):
    answer = ''
    if len(p) == 0:
        return answer
    if is_right(p):
        return p
    split_idx = _split(p)
    u, v = p[:split_idx+1], p[split_idx+1:]
    if is_right(u):
        answer += u
        return answer + solution(v)
    answer = '('
    answer += solution(v)
    answer += ')'
    u = list(u)
    u.pop(0)
    u.pop()
    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        elif u[i] == ')':
            u[i] = '('
    if u:
        u = ''.join(u)
    else:
        u = ''

    answer += u
    return answer
