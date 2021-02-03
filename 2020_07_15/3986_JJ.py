n = int(input())
ans = n

for _ in range(n):
    char_list = list(input())
    #print(char_list)
    stack = []
    stack.append(char_list[0])
    for i in range(1,len(char_list)):
        if stack and stack[len(stack)-1] == char_list[i]:
            stack.pop()
        else :
            stack.append(char_list[i])
    if len(stack) != 0:
        ans = ans - 1
print(ans)