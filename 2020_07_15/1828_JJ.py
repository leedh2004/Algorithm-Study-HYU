import queue

c = int(input())
n = [0]*c
coord = []
addj = [[987654321]*c for _ in range(c)]

# 입력
for i in range(c):
    tmp = list(map(int,input().split()))
    n[i] = tmp[0]
    tmp = tmp[1:]
    argc = 3
    tmp_list = [tmp[i * argc:(i + 1) * argc] for i in range((len(tmp) + argc - 1) // argc )]
    tuple_list = [tuple(l) for l in tmp_list]
    coord.append(tuple_list)


for i in range(c):
    addj[i][i] = 0

# 인접 여부 검사
for i in range(c-1):
    for j in range(i+1,c):
        tmp = set(coord[i]) - set(coord[j])
        #print(tmp)
        if len(tmp) < n[i]-1:
            addj[i][j] = 1
            addj[j][i] = 1


# 완전 탐색
for i in range(c):
    for j in range(c):
        for k in range(c):
            if addj[i][k] + addj[k][j] < addj[i][j] :
                addj[i][j] = addj[i][k] + addj[k][j] 

# print(addj)
q = int(input())
for _ in range(q):
    start,end = map(int,input().split())
    print(addj[start-1][end-1])


        

    




