from copy import deepcopy
def solution(key, lock):
    M, N = len(key), len(lock)
    for _ in range(4):
        # 열쇠 90도 회전
        key = [[ key[M - 1 - x][y] for x in range(M)] for y in range(M) ]
        for y in range(-M+1, N):
            for x in range(-M+1, N):
                L = deepcopy(lock)
                flag = False
                for dy in range(M):
                    for dx in range(M):
                        if y + dy < 0 or y + dy >= N or x + dx >= N or x + dx< 0:
                            continue
                        elif key[dy][dx] + lock[y+dy][x+dx] == 1:
                            L[y+dy][x+dx] = 1
                            continue
                        else:
                            # flag = True가 되면 만족할 수 없는 케이스므로 멈춤.
                            flag = True
                            break
                    if flag:
                        break
                if flag:
                    continue
                S = sum([i.count(0) for i in L])
                if S == 0:
                    return True
    return False