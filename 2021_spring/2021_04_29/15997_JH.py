import sys
input = sys.stdin.readline
from collections import defaultdict

def dfs(count, prob):
    global match, score

    if count == 6 :
        L = [ (sco, team) for (team, sco) in score.items() ]
        L.sort(reverse=True)

        if L[0][0] == L[1][0] == L[2][0] == L[3][0] :
            for i in range(4):
                result[L[i][1]] += prob*(1/2)
            return

        elif L[0][0] > L[1][0] == L[2][0] == L[3][0] :
            result[L[0][1]] += prob 
            for i in range(1,4,1):
                result[L[i][1]] += prob*(1/3)
            return

        elif L[0][0] == L[1][0] == L[2][0] :
            for i in range(3):
                result[L[i][1]] += prob*(2/3)
            result[L[3][1]] += 0
            return

        elif L[0][0] > L[1][0] == L[2][0] :
            result[L[0][1]] += prob
            for i in range(1,3,1):
                result[L[i][1]] += prob*(1/2)
            result[L[3][1]] += 0
            return

        else :
            for i in range(0,2,1):
                result[L[i][1]] += prob
            for i in range(2,4,1):
                result[L[i][1]] += 0
            return

    score[match[count][0]] += 3
    dfs(count+1, prob*match[count][2])
    score[match[count][0]] -= 3

    score[match[count][0]] += 1
    score[match[count][1]] += 1
    dfs(count+1, prob*match[count][3])
    score[match[count][0]] -= 1
    score[match[count][1]] -= 1

    score[match[count][1]] += 3
    dfs(count+1, prob*match[count][4])
    score[match[count][1]] -= 3





teams = list(input().strip().split())
match = []

for i in range(6):
    winer, loser, p1, p2, p3 = input().strip().split()
    p1,p2,p3 = map(float, [p1,p2,p3])
    
    match.append([winer, loser, p1, p2, p3])

score = {team : 0 for team in teams}
result = {team : 0 for team in teams}

dfs(0, 1)

for team in teams :
    print(result[team])


# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# teams = list(input().strip().split())
# len_teams = len(teams)
# prob = {team : 0 for team in teams}


# for i in range(len_teams*(len_teams-1)//2):
#     winer, loser, p1, p2, p3 = input().strip().split()
#     p1,p2,p3 = map(float, [p1,p2,p3])
    
#     prob[winer] += (p1*3 + p2*1 + p3*0)
#     prob[loser] += (p1*0 + p2*1 + p3*3)

# # print(prob)

# prob2 = defaultdict(list)

# for (team, pro) in prob.items() :
#     prob2[pro].append(team)

# # print(prob2)

# max_prob = max(prob2)
# len_first_team = len(prob2[max_prob])

# for team in prob :
#     prob[team] = 0.0

# if len_first_team >= 2 :
#     tmp_prob = 1.0/len_first_team
#     for team in prob2[max_prob]:
#         prob[team] = tmp_prob

# else :
#     prob[prob2[max_prob][0]] = 1.0
#     del prob2[max_prob]
    
#     max_prob = max(prob2)
#     len_second_team = len(prob2[max_prob])

#     tmp_prob = 1.0/len_second_team
#     for team in prob2[max_prob]:
#         prob[team] = tmp_prob

# for team in teams :
#     print("{0:.10f}".format(prob[team]))


# KOREA CCC BBB AAA
# KOREA CCC 0.0 1.0 0.0
# AAA BBB 0.0 1.0 .0
# AAA KOREA 0.0 0.0 1.0
# CCC BBB 0.0 1.0 0.0
# KOREA BBB 1.0 0.0 0.0
# CCC AAA 0.5 0.0 0.5