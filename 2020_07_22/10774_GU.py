import sys

J = int(sys.stdin.readline())
A = int(sys.stdin.readline())
jersey = [0 for _ in range(J+1)]
player = [0 for _ in range(J+1)]
table = str.maketrans('SML','123')
table2 = str.maketrans('SML','123')
for i in range(J):
    jersey[i+1] = int(sys.stdin.readline().rstrip().translate(table))
for i in range(A):
    s,n = sys.stdin.readline().split()
    n = int(n)
    if player[n] == 0:
        player[n] = int(s.translate(table2))
    else:
        if player[n] > int(s.translate(table2)):
            player[n] = int(s.translate(table2))
zeros = player.count(0)
cnt = 0
for i in range(J+1):
    tmp = jersey[i] - player[i]
    if tmp >= 0: cnt += 1
print(cnt - zeros)