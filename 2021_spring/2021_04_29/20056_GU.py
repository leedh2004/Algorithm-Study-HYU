import sys
from copy import deepcopy


def move(fireball):
    global N
    y, x = fireball[0], fireball[1]
    ny, nx = 0, 0
    if fireball[4] == 0:
        ny, nx = y-fireball[3], x
    elif fireball[4] == 1:
        ny, nx = y-fireball[3], x+fireball[3]
    elif fireball[4] == 2:
        ny, nx = y, x+fireball[3]
    elif fireball[4] == 3:
        ny, nx = y+fireball[3], x+fireball[3]
    elif fireball[4] == 4:
        ny, nx = y+fireball[3], x
    elif fireball[4] == 5:
        ny, nx = y+fireball[3], x - fireball[3]
    elif fireball[4] == 6:
        ny, nx = y, x-fireball[3]
    elif fireball[4] == 7:
        ny, nx = y-fireball[3], x - fireball[3]

    # if ny >= 0:
    #     ny %= N
    # else:
    #     ny = N - abs(ny) % N
    # if nx >= 0:
    #     nx %= N
    # else:
    #     nx = N - abs(nx) % N
    ny = (ny+N) % N
    nx = (nx+N) % N

    fireball[0], fireball[1] = ny, nx

    return ny, nx


N, M, K = map(int, sys.stdin.readline().split())
grid = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    grid[r-1][c-1].append([r-1, c-1, m, s, d])

for _ in range(K):
    new_grid = [[[] for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) > 0:
                for fb in grid[i][j]:
                    ny, nx = move(fb)
                    new_grid[ny][nx].append(fb)

    for i in range(N):
        for j in range(N):
            if len(new_grid[i][j]) > 1:
                mass = 0
                velocity = 0
                UDLR = True
                is_odd = True
                for x, fb in enumerate(new_grid[i][j]):
                    if x == 0:
                        if fb[4] % 2 == 0:
                            is_odd = False
                    else:
                        if (fb[4] % 2 == 0 and is_odd) or (fb[4] % 2 == 1 and not is_odd):
                            UDLR = False
                    mass += fb[2]
                    velocity += fb[3]
                mass //= 5
                velocity //= len(new_grid[i][j])

                if mass == 0:
                    new_grid[i][j].clear()
                else:
                    if UDLR:
                        new_grid[i][j] = [[i, j, mass, velocity, 0], [i, j, mass, velocity, 2], [
                            i, j, mass, velocity, 4], [i, j, mass, velocity, 6]]
                    else:
                        new_grid[i][j] = [[i, j, mass, velocity, 1], [i, j, mass, velocity, 3], [
                            i, j, mass, velocity, 5], [i, j, mass, velocity, 7]]

    grid = deepcopy(new_grid)
    # print(grid)

total_mass = 0
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            for fb in grid[i][j]:
                total_mass += fb[2]
print(total_mass)
