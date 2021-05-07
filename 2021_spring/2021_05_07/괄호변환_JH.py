from collections import deque

def check(s):
    if s[-1] =='(':
        return False
    count = 0
    for i in s[::-1] :
        if i == ')':
            count += 1
        else :
            count -= 1
    if count == 0 :
        return True
    else :
        return False

def solution(p):
    if not p :
        return p
    string = deque(p)

    u = []
    count = 0
    while True : 
        t = string.popleft()
        if t == '(':
            count += 1
        else :
            count -= 1
        u.append(t)
        if count == 0:
            break
    v = []
    while string :
        v.append(string.popleft())

    if check(u) :
        u += solution(v)
        return "".join(u)

    else :
        result = ['('] + list(solution(v)) + [')'] + [ ')' if i == '(' else '(' for i in u[1:-1]  ]
        return "".join(result)
        


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
