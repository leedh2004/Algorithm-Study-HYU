import sys

N, M = map(int,sys.stdin.readline().split())

paper = [[0]* (501) for _ in range(501)]

for i in range(N):
    paper[i] = list(map(int,sys.stdin.readline().split()))

case = []
for i in range(N):
    for j in range(M):
        if j+3 < M: # 0 0 0 0
            case.append(paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i][j+3])
        if i+3 < N: # spin
            case.append(paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+3][j])
        if i+1 < N and j+1 < M: # square
            case.append(paper[i][j]+paper[i][j+1]+paper[i+1][j]+paper[i+1][j+1])
        if i+2 <N and j+1 < M: # point at left upper point (3x2)
            case.append(paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+2][j+1])
            case.append(paper[i][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i+2][j+1])
            case.append(paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i][j+1])
            case.append(paper[i][j]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j+1])
            case.append(paper[i][j]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j])
        if i+2 < N and j-1 >= 0 : # point at right upper point(3x2)
            case.append(paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+2][j-1])
            case.append(paper[i][j]+paper[i+1][j]+paper[i+1][j-1]+paper[i+2][j])
            case.append(paper[i][j]+paper[i+1][j]+paper[i+1][j-1]+paper[i+2][j-1])
        if i+1 < N and j+2 < M: # point at left upper point (2x3)
            case.append(paper[i][j]+paper[i+1][j]+paper[i][j+1]+paper[i][j+2])
            case.append(paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i+1][j+2])
            case.append(paper[i][j]+paper[i+1][j]+paper[i+1][j+1]+paper[i+1][j+2])
            case.append(paper[i][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i+1][j+2])
            case.append(paper[i][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i][j+2])
        if i-1 >= 0 and j+2 < M: # point at left bottom point (2x3)
            case.append(paper[i][j]+paper[i][j+1]+paper[i-1][j+1]+paper[i-1][j+2])
            case.append(paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i-1][j+2])
            case.append(paper[i][j]+paper[i][j+1]+paper[i-1][j+1]+paper[i][j+2])
print(max(case))
                    
            
