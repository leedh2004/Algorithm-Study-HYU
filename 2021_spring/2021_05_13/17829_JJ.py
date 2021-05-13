import sys

input = sys.stdin.readline

def getSecond(arr):
    sortedArr = sorted(arr,reverse=True)
    return sortedArr[1]

n = int(input())
oldtable = []
for i in range(n):
    oldtable.append(list(map(int,input().split())))

dx = [0,0,1,1]
dy = [0,1,0,1]
nowN = n
while 1:
    newTable = []
    for row in range(0,nowN-1,2):
        newRow = []
        for columm in range(0,nowN-1,2):
            tmp = []
            for j in range(4):
                tmp.append(oldtable[row+dx[j]][columm+dy[j]])
            newRow.append(getSecond(tmp))
        newTable.append(newRow)
    oldtable = newTable
    nowN = len(newTable[0])
    if nowN == 1:
        print(newTable[0][0])
        break