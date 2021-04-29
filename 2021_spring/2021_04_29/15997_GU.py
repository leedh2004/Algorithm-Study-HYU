import sys


# 승자 승점 3 비기면 1 지면 0
# 6게임을 치른다 3^6가지수
# cnt 경기 num
def dfs(prob, cnt, vp):
    # 6경기 모두 끝
    if cnt == 6:
        sorted_vp = sorted(vp.items(), key=lambda x: x[1], reverse=True)

        # 네 팀 모두 승점 같을 때
        if sorted_vp[0][1] == sorted_vp[1][1] == sorted_vp[2][1] == sorted_vp[3][1]:
            probs[sorted_vp[0][0]] += prob * 0.5
            probs[sorted_vp[1][0]] += prob * 0.5
            probs[sorted_vp[2][0]] += prob * 0.5
            probs[sorted_vp[3][0]] += prob * 0.5
        # 상위 세 팀 승점 같을 때
        elif sorted_vp[0][1] == sorted_vp[1][1] == sorted_vp[2][1]:
            probs[sorted_vp[0][0]] += prob * (2/3)
            probs[sorted_vp[1][0]] += prob * (2/3)
            probs[sorted_vp[2][0]] += prob * (2/3)
        # 하위 세 팀 승점 같을 때
        elif sorted_vp[1][1] == sorted_vp[2][1] == sorted_vp[3][1]:
            probs[sorted_vp[0][0]] += prob
            probs[sorted_vp[1][0]] += prob * (1/3)
            probs[sorted_vp[2][0]] += prob * (1/3)
            probs[sorted_vp[3][0]] += prob * (1/3)
        # 2,3 등 승점 같을 때
        elif sorted_vp[1][1] == sorted_vp[2][1]:
            probs[sorted_vp[0][0]] += prob
            probs[sorted_vp[1][0]] += prob * 0.5
            probs[sorted_vp[2][0]] += prob * 0.5
        else:
            probs[sorted_vp[0][0]] += prob
            probs[sorted_vp[1][0]] += prob
        return
        # win
    vp[info[cnt][0]] += 3
    dfs(prob * info[cnt][2], cnt+1, vp)
    vp[info[cnt][0]] -= 3

    # draw
    vp[info[cnt][0]] += 1
    vp[info[cnt][1]] += 1
    dfs(prob * info[cnt][3], cnt+1, vp)
    vp[info[cnt][0]] -= 1
    vp[info[cnt][1]] -= 1

    # lose
    vp[info[cnt][1]] += 3
    dfs(prob * info[cnt][4], cnt+1, vp)
    vp[info[cnt][1]] -= 3


countries = list(sys.stdin.readline().split())
info = []
vp = {country: 0 for country in countries}
probs = {country: 0 for country in countries}
for i in range(6):
    info.append(list(sys.stdin.readline().split()))
    info[i][2] = float(info[i][2])
    info[i][3] = float(info[i][3])
    info[i][4] = float(info[i][4])
dfs(1, 0, vp)
for country in countries:
    print(probs[country])
"""
for i in range(4):
    winner = countries[i]
    prob = 0
    # 3승
    tmp = 1
    for j in range(3):
        tmp *= info[winner][j][1]
    prob += tmp
    # 2승 1무 (무승부하지 않은 사람이 2승X + 무승부한 사람이 2승 * 0.5)
    # 무승부 고르기 j
    for j in range(3):
        moo = info[winner][j][0]
        tmp = 1
        # i가 2승 1무할 확률
        tmp = info[winner][j][2] * \
            info[winner][(j+1) % 3][1] * info[winner][(j+2) % 3][1]
        # 무승부 하지 않은 사람이 2승 X
        tmp2 = 1
        for k in range(3):
            if info[moo][k][0] == winner:
                continue
            else:
                tmp2 *= info[moo][k][1]
        prob += tmp * ((1-tmp2)+(tmp2*0.5))

    # 2승 1패
    # 패 고르기 j / j가 (3승, 2승 1무X)  2승 1패일 때 (j+1이 2승 1패, j+2가 2승 1패 or 둘 다 그 이하)
    for j in range(3):
        lose = info[winner][j][0]
        tmp = 1
        # i가 2승 1패할 확률
        tmp = info[winner][j][3] * \
            info[winner][(j+1) % 3][1] * info[winner][(j+2) % 3][1]
"""
