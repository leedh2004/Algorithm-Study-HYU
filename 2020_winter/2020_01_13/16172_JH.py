import re

def failure_func(K) :
    n = len(K)
    begin, m = 1,0
    f = [ 0 for _ in range(n) ]

    while begin+m < n :
        if K[begin+m] == K[m] :
            m += 1
            f[begin+m-1] = m 
        else :
            if m == 0 :
                begin += 1
            else :
                begin += m-f[m-1]
                m = f[m-1]
    return f

def KMP(S,K):
    s_len = len(S)
    k_len = len(K)
    begin, m = 0,0
    f = failure_func(K)
    result = []

    while begin <= s_len - k_len :
        if m < k_len and S[begin+m] == K[m] :
            m += 1
            if m == k_len :
                result.append(begin)
        else :
            if m == 0 :
                begin += 1
            else :
                begin += m-f[m-1]
                m = f[m-1]

    return result

tmp_S = input()
S = re.sub('[0-9]', "", tmp_S)
K = input()

print(len(KMP(S,K)))