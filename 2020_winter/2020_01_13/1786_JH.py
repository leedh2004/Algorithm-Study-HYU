def failure_func(S):
    n = len(S)
    begin,m = 1,0
    f = [ 0 for _ in range(n) ]

    while begin+m < n :
        if S[begin+m] == S[m] :
            m += 1
            f[begin+m-1] = m
        else :
            if m == 0 :
                begin += 1
            else :
                begin += m-f[m-1]
                m = f[m-1]
    return f

def KMP(T,P):
    t_len = len(T)
    p_len = len(P)

    begin, m = 0,0 
    f = failure_func(P)

    result = []

    while begin <= t_len-p_len :
        if m < p_len and T[begin+m] == P[m] :
            m += 1
            if m == p_len :
                result.append(begin+1)
        else :
            if m == 0 :
                begin += 1
            else :
                begin += m-f[m-1]
                m = f[m-1]
    return result



T = input()
P = input()

result = KMP(T,P)
print(len(result))
print(*result)