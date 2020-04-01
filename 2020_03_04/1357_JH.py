X,Y = input().split()
Z = int(X[::-1])+int(Y[::-1])  #rev 하고 int로 바꿔서 int 값 저장
print(int(str(Z)[::-1])) #str로 바꿔서 rev하고 int 로 저장