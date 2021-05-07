def rotate_90(k):
    M = len(k)
    ret = [[0] * M for _ in range(M)]

    for r in range(M):
        for c in range(M):
            ret[c][M-1-r] = k[r][c]
    return ret


def solution(key, lock):
    answer = True
    M, N = len(key), len(lock)
    grid = [[-1] * (2*M+N) for _ in range(2*M + N)]
    keys = [key]
    for i in range(3):
        tmp = rotate_90(keys[-1])
        keys.append(tmp)
    lock_slot = []
    lock_cnt = 0
    for i in range(N):
        for j in range(N):
            grid[M+i][M+j] = lock[i][j]
            if lock[i][j] == 0:
                lock_slot.append([M+i, M+j])
                lock_cnt += 1
    # 다 열려있는 경우(자물쇠)
    if lock_cnt == 0:
        return True
    for _key in keys:
        key_slot = []
        for i in range(M):
            for j in range(M):
                if _key[i][j]:
                    key_slot.append([i, j])
        for ks in key_slot:
            for ls in lock_slot:
                dy, dx = ls[0]-ks[0], ls[1]-ks[1]
                cnt = 0
                match = True
                grid2 = [[-1] * (2*M+N) for _ in range(2*M + N)]
                for i in range(M):
                    for j in range(M):
                        grid2[dy+i][dx+j] = _key[i][j]
                for i in range(M):
                    for j in range(M):
                        if grid2[dy+i][dx+j] == 1 and grid[dy+i][dx+j] == 1:
                            match = False
                            break
                        elif grid2[dy+i][dx+j] == 1 and grid[dy+i][dx+j] == 0:
                            cnt += 1
                    if not match:
                        break

                if match and cnt == lock_cnt:
                    return True

    return False
