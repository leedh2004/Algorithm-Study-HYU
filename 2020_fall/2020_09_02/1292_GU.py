import sys

A,B= map(int,sys.stdin.readline().split())
ends=[0,0]
for i in range(2,1001):
    tmp = ends[-1]+i
    if tmp < 1001:
        if ends[-1] < A-1 <= tmp:
            A_idx = len(ends) # A번째 숫자
        if ends[-1] < B-1 <= tmp:
            B_idx = len(ends) # B번째 숫자
        ends.append(tmp)
    else:
        ends.append(tmp) 
        break
if A==B: print(A_idx)
else:
    if A_idx == B_idx: print(A_idx * (B-A +1))
    else:
        res = 0
        for i in range(A_idx+1,B_idx):
            res += (i ** 2)
        if A-1 in ends:
            res += A-1
        else:
            res += A_idx * (ends[A_idx] - (A-1))
        #print(res)
        if B-1 in ends:
            res += ((B-1) ** 2)
        else:
            res += B_idx * (B-1 - ends[B_idx-1])
        print(res)

