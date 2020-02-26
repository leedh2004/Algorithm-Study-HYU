def fibonach(n):
    f_1=0
    f_2=1
    if(n==0): return 0
    elif(n==1): return 1
    for i in range(n-1):
        f_n = f_1 + f_2
        f_1 = f_2
        f_2 = f_n
    return f_n
T = int(input())
list_ = []
append = list_.append
for i in range(T):
    append(int(input()))

for i in range(T):
    if(list_[i] == 0):
        print (1,0)
    elif(list_[i] == 1):
        print (0,1)
    else:
        print(fibonach(list_[i]-1),fibonach(list_[i]))

