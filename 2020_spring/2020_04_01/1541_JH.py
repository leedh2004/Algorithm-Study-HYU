L = list(str(input())) #너무 c스럽게 짠듯, 아래 인터넷에서 긁어온 코드 보는게 좋을듯
opra = list()
oper = list()
tmp = ""    #operand, operator 나누기
for i in L :
    if i != '+' and i != '-' :
        tmp += i
    else :
        opra.append(int(tmp))
        tmp = ""
        oper.append(i)
opra.append(int(tmp))  #마지막은 무조건 숫자, 이거 넣어줘야함. 위에 루프에서는 마지막 숫자 만들고 더 안돌고 끝나니까 필요

lop = len(oper)   #operator의 길이
for i in range(lop) : #최적의 괄호를 치는법 찾기
    if oper[i] == '-':
        for j in range(i+1,lop,1):
            if oper[j] == '+':
                oper[j] = '-'
            else :
                break

result = opra[0]
for i in range(lop) : #결과값 계산하기
    if oper[i] == '+':
        result += opra[i+1]
    else :
        result -= opra[i+1]

print(result)



# arr = input().split('-')  #마이너스 기준으로 자름     인터넷 코드, 이게 파이썬이다...
# s = 0
# for i in arr[0].split('+'):  #위에 자른 식 안에서 +를 기준으로 자르면서 더해줌
#     s += int(i)
# for i in arr[1:]:  #맨 처음(0)은 앞에 -가 없으니까 전체 값을 줄이는 역활x, 1번째 배열부터
#     for j in i.split('+'):  #+를 기준으로 짜름, 즉 숫자만 보겠다는 의미
#         s -= int(j)
# print(s)