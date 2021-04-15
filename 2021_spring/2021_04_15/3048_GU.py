import sys

N1, N2 = map(int, sys.stdin.readline().split())
line = []
# 왼-> 오
A1 = list(sys.stdin.readline().rstrip())
A1.reverse()
line.extend(A1)
A1.reverse()
# 오 -> 왼
A2 = list(sys.stdin.readline().rstrip())
line.extend(A2)
T = int(sys.stdin.readline())

time = 0

for _ in range(T):
    i = 0
    while i < N1+N2:
        if i+1 < N1+N2:
            # or (line[i] in A2 and line[i+1] in A1) -> 방향 지켜야 XX
            if (line[i] in A1 and line[i+1] in A2):
                tmp = line[i+1]
                line[i+1] = line[i]
                line[i] = tmp

                i += 2
                continue
            else:
                i += 1
        else:
            i += 1
print(''.join(line))
