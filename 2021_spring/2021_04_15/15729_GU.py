import sys

N = int(sys.stdin.readline())
note = list(map(int, sys.stdin.readline().split()))
cur = [0 for _ in range(N)]
cnt = 0
for i in range(N):
    if cur[i] != note[i]:
        cnt += 1
        if i+1 < N:
            if cur[i+1]:
                cur[i+1] = 0
            else:
                cur[i+1] = 1

        if i+2 < N:
            if cur[i+2]:
                cur[i+2] = 0
            else:
                cur[i+2] = 1

print(cnt)

# if i+1 < N and cur[i+1:] == note[i+1:]: break
