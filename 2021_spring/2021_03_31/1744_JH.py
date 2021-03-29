import sys
input = sys.stdin.readline

N = int(input())
plus, minus, zero = [], [], False
result = 0

for i in range(N):
    tmp = int(input())
    if tmp > 0 :
        plus.append(tmp)
    elif tmp < 0 :
        minus.append(tmp)
    else :
        zero = True

plus.sort(reverse=True)
minus.sort()

len_p, len_m = len(plus), len(minus)


for i in range(0, len_m, 2) :
    try :
        result += minus[i]*minus[i+1]
    except :
        if not zero :
            result += minus[len_m-1]


for i in range(0, len_p, 2) :
    try :
        if plus[i+1] == 1 :
            result += (plus[i] + plus[i+1])
        else :
            result += plus[i]*plus[i+1]
    except :
        result += plus[len_p-1]


print(result)


# 4
# -1
# 2
# 1
# 3
# 답 : 6

# --------------------------------------------------------------------

# case1. 양수기준 - (양수가 짝수개일때) 내림차순으로 정렬했을때 큰값 2개씩 곱해서 답을 도출하는가

# input : 4 9 4 2 7
# output : 71

# --------------------------------------------------------------------

# case2. 양수기준 - (양수가 홀수개일때) 내림차순으로 정렬했을 때 큰값 2개씩 곱한 후 마지막에 숫자를 더해서 답을 도출하는가
# input : 7 9 7 4 2 8 8 7
# output : 158

# --------------------------------------------------------------------

# case3. 음수기준 - 오름차순으로 정렬했을때 작은값 2개씩 묶어서 답을 도출하는가 (이유 : 음수는 작을수록 두 수를 곱했을때 커지므로)
# input : 4 -9 -11 -2 -4
# output : 107

# --------------------------------------------------------------------

# case4. 0이 존재하면서 음수의 개수가 홀수개 일때 마지막 음수를 0으로 처리하는지
# input : 8 -10 -5 0 0 0 -11 -9 -2
# output : 155

# --------------------------------------------------------------------

# case5. 1이 존재할때 1은 다른수와 곱하지 않고 바로 더하는지 (이유 : 1보다 큰 수 x와 1이 주어진다면 두수를 곱하는것보다 따로 더해주는게 더 크다)
# input : 5 5 4 1 1 1
# output : 23