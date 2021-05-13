def solution(str1, str2):
    A,B = [],[]
    for (first, second) in zip(str1, str1[1:]) :
        tmp = "".join([first, second])
        if tmp.isalpha() :
            A.append(tmp.lower())

    for (first, second) in zip(str2, str2[1:]) :
        tmp = "".join([first, second])
        if tmp.isalpha() :
            B.append(tmp.lower())
    
    len_A, len_B = len(A), len(B)

    inter = 0

    if len_A > len_B :
        for b in B :
            if b in A :
                A.remove(b)
                inter += 1

    else :
        for a in A :
            if a in B :
                B.remove(a)
                inter += 1

    uni = len(A+B)

    if uni == 0:
        return 65536

    answer = int(inter/uni*65536)
    return answer