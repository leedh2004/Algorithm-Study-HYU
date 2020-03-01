N = int(input())

Aj = list(map(int,input().split()))

length = [1]
minimum = []
minimum.append(Aj[0])
for i in range(N):
    for j in range(len(minimum)):
        if Aj[i] > minimum[j]:
            length[j] +=1
            minimum[j] = Aj[i]
        elif Aj[i] < minimum[j]:
            minimum.append(Aj[i])
            length.append(1)

print(max(length))
