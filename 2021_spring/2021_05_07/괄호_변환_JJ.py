def solution(p):
    return recur(p)


def recur(p):
    if p == '':
        return ''
    u,v = sliceToUV(p)
    
    if validation(u):
        return u + recur(v)
    
    u = u[1:-1]
    newu = ''
    
    for c in u:
        if c == '(':
            newu = newu + ')'
        else :
            newu = newu + '('
            
    return '('+recur(v)+')' + newu

def sliceToUV(p):
    s = 0
    uvIdx = 0
    for idx in range(len(p)):
        if p[idx] == '(':
            s = s + 1
        elif p[idx] == ')':
            s = s - 1

        if s == 0:
            uvIdx = idx
            break
            
    return p[:uvIdx+1],p[uvIdx+1:]

def validation(p):
    s = 0
    for idx in range(len(p)):
        if p[idx] == '(':
            s = s + 1
        elif p[idx] == ')':
            s = s - 1
            if s < 0 :
                return False
    return True
                