n = int(input())
result = 0

for i in range(n):
    string = list(input())
    stack = []
    
    for j in range(len(string)):
        tmp = string.pop()
        if not stack : 
            stack.append(tmp)
        
        else :
            if tmp == stack[-1]:
                stack.pop()
            else :
                stack.append(tmp)
    
    if not stack :
        result += 1

print(result)