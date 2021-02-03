import sys

N = int(sys.stdin.readline().rstrip())

A = list(map(int,input().split()))
B,C = map(int,sys.stdin.readline().split())


cnt = 0
for i in range(N):
    if A[i] <= B:
        cnt += 1
        continue
    else:
        cnt += int((A[i]-B)/C) + 1
        if (A[i]-B)%C != 0:
            cnt +=1
print(cnt)
