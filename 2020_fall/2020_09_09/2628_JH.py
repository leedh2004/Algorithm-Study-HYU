height,width = map(int,input().split())
N = int(input())
w,h = [0,width], [0,height]
result = -1
for i in range(N):
    a,b = map(int,input().split())
    if a == 0 :
        w.append(b)
    else :
        h.append(b)
w.sort()
h.sort()

for i in range(len(w)-1):
    tmp_w = w[i+1]-w[i]
    for j in range(len(h)-1):
        tmp_h = h[j+1]-h[j]
        result = max(result, tmp_w*tmp_h )

print(result)