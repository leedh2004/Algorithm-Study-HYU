def div(w):
        # 빈 문자열인 경우
        if w == '':
            return ''
        s = 0
        u, v = '', ''
        # u, v 분리
        for i, c in enumerate(w):
            if c == '(':
                s += 1
            elif c == ')':
                s -= 1
            u += c
            if s == 0:
                break
        v = w[i+1:]
        
        # u가 올바른 문자열인지 확인
        s = 0 
        flag = True
        for c in u:
            if c == '(':
                s += 1
            elif c == ')':
                s -= 1
                if s < 0:
                    flag = False
                    break
        
        # 올바른 문자열인 경우
        if flag:
            u = u + div(v)
            return u
        # 올바른 문자열이 아닌 경우
        else:
            k = '(' + div(v) + ')'
            u = u[1:-1]
            u = "".join(['(' if c == ')' else ')' for c in u])
            return k + u
        
def solution(p):            
    answer = div(p)    
    return answer