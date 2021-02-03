import sys

# 현재 2000점이며,랭크게임 20번
# 소수점 아래 9번째 자리에서 반올림하여 소수점 8자리까지 출력
W,L,D = map(float,sys.stdin.readline().split())
score = [0 for i in range(41)]
cur = []
if D > 0:
    score[20] += D
    cur.append(20)
if W > 0:
    score[21] += W
    cur.append(21)
if L > 0:
    score[19] += L
    cur.append(19)

for i in range(19):
    length = len(cur)
    need_to_add = []
    for j in range(length):
        now = cur.pop(0)
        now_score = score[now]
        score[now] = 0
        # score 바로 바꿔주면 이 for문돌때 다음 인덱스에 바로 영향 미침
        if W > 0:
            #score[now+1] += (now_score * W)
            need_to_add.append([now+1,now_score*W])
            cur.append(now+1)
        if L > 0:
            #score[now-1] += (now_score * L)
            need_to_add.append([now-1,now_score*L])
            cur.append(now-1)
        if D > 0:
            #score[now] += (now_score * D)
            need_to_add.append([now,now_score*D])
            cur.append(now)
    for j in range(len(need_to_add)):
        idx, percentage = need_to_add[j]
        score[idx] += percentage
    cur = list(set(cur))
print('%.8f' % (sum(score[:10])/sum(score)))
print('%.8f' % (sum(score[10:20])/sum(score)))
print('%.8f' % (sum(score[20:30])/sum(score)))
print('%.8f' % (sum(score[30:40])/sum(score)))
print('%.8f' % score[40])


# 시간이 너무 오래 걸린다..
# score = []
# if W > 0: score.append([2050,W])
# if L > 0: score.append([1950,L])
# if D > 0: score.append([2000,D])
# print(score)
# for i in range(19):
#     print(i)
#     length = len(score)
#     for j in range(length):
#         cur, percentage = score.pop(0)
#         if percentage * W > 0:
#             score.append([cur+50,percentage*W])
#         if percentage * L > 0:
#             score.append([cur-50,percentage*L])
#         if percentage * D > 0:
#             score.append([cur,percentage * D])

# print(score)




