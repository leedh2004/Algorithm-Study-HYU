N = int(input())
B = [ list(map(int, input().split())) for _ in range(N) ]
D = [(0, 0), (1, 0), (0, 1), (1, 1)]
while len(B) != 1:
    new_B = [ [] for _ in range(len(B) // 2)]
    i = 0
    for y in range(0, len(B), 2):
        for x in range(0, len(B), 2):
            lis = []
            for dy, dx in D:
                ny, nx = y + dy, x + dx
                lis.append(B[ny][nx])
            lis = sorted(lis)
            new_B[i].append(lis[2])
        i += 1
    B = new_B
print(B[0][0])