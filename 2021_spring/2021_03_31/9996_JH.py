import sys
input = sys.stdin.readline

N = int(input())
pat = input().strip()
flag = 0
if pat[0] == '*':
    flag = -1
elif pat[-1] == '*':
    flag = 1
else :
    flag = 0

sub_pat = pat.split('*')

for _ in range(N):
    name = input().strip()
    tmp_flag = True
    if flag == -1 :
        L = len(sub_pat[1])
        if len(name) < L :
            tmp_flag = False
        else :
            for i in range(-1, -L-1, -1):
                try :
                    if name[i] != sub_pat[1][i]:
                        tmp_flag = False
                        break
                except :
                    tmp_flag = False
                    break
    elif flag == 1 :
        L = len(sub_pat[0])
        if len(name) < L :
            tmp_flag = False
        else :
            for i in range(0, L, 1):
                try :
                    if name[i] != sub_pat[0][i] :
                        tmp_flag = False
                        break
                except :
                    tmp_flag = False
                    break
    else :
        L1, L2 = len(sub_pat[0]), len(sub_pat[1])
        if len(name) < L1+L2 :
            tmp_flag = False
        else :
            for i in range(0, len(sub_pat[0]), 1):
                try :
                    if name[i] != sub_pat[0][i] :
                        tmp_flag = False
                        break
                except :
                    tmp_flag = False
                    break
            if tmp_flag :
                for i in range(-1, -len(sub_pat[1])-1, -1):
                    try :
                        if name[i] != sub_pat[1][i]:
                            tmp_flag = False
                            break
                    except :
                        tmp_flag = False
                        break

    if tmp_flag :
        print('DA')
    else :
        print('NE')