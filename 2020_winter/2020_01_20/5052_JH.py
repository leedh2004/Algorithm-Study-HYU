import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        curr_node = self.head
        for c in string :
            if c not in curr_node.children :
                curr_node.children[c] = Node(c)
            curr_node = curr_node.children[c]
        curr_node.data = string

    def search(self, string):
        curr_node = self.head
        for c in string :
            if c not in curr_node.children :
                return False
            curr_node = curr_node.children[c]
        
        if curr_node.data == None :
            return False
        else :
            return True
    
    def solution(self, string):
        curr_node = self.head
        for c in string :
            curr_node = curr_node.children[c]
        if curr_node.children :
            return True
        else :
            return False

t = int(input())

for a in range(t):
    n = int(input())
    phone_nums = []
    trie = Trie()

    for i in range(n):
        nums = input().strip()
        phone_nums.append(nums)
        trie.insert(nums)
    
    flag = False
    for i in phone_nums :
        flag = trie.solution(i)
        if flag == True:
            print('NO')
            break
    if flag == False:
        print('YES')



# import sys
# input = sys.stdin.readline

# class Node(object):
#     def __init__(self, key, data=None):
#         self.key = key
#         self.data = data
#         self.children = {}

# class Trie(object):
#     def __init__(self):
#         self.head = Node(None)

#     def insert(self, string):
#         curr_node = self.head

#         for c in string :
#             if c not in curr_node.children :
#                 curr_node.children[c] = Node(c)
#             curr_node = curr_node.children[c]

#         curr_node.data = string

#     def search(self, string):
#         curr_node = self.head

#         for c in string :
#             if c in curr_node.children :
#                 curr_node = curr_node.children[c]
#             else :
#                 return False

#         if curr_node.data != None :
#             return True
#         else :
#             return False

#     def solution(self, string):
#         curr_node = self.head
#         for c in string :
#             curr_node = curr_node.children[c]

#         if curr_node.children :
#             return False
#         else :
#             return True


# t = int(input())

# for a in range(t):
#     n = int(input())
#     phone_nums = [ ]
#     trie = Trie()
#     flag = True

#     for i in range(n):
#         num = input().strip()
#         phone_nums.append(num)
#         trie.insert(num)

#     for i in range(n):
#         flag = trie.solution(phone_nums[i])
#         if flag == False :
#             print('NO')
#             break
#     if flag : 
#         print('YES')