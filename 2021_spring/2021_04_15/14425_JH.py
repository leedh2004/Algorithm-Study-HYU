# import sys
# input = sys.stdin.readline

# class Node():
#     def __init__(self, key, data=None):
#         self.key = key
#         self.data = data
#         self.children = {}

# class Trie():
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
#             if c not in curr_node.children :
#                 return False
#             curr_node = curr_node.children[c]

#         if curr_node.data :
#             return True
#         else :
#             return False

# N, M = map(int, input().strip().split())
# S = Trie()
# result = 0

# for i in range(N) :
#     S.insert(input().strip())

# for i in range(M) :
#     if S.search(input().strip()) :
#         result += 1

# print(result)

            


# 이게 훨씬 빠름.
# 파이썬 dictinary의 key로는 상당히 긴 값이 들어갈 수 있다고 함(메모리와 관련이 있다는 것 같음)
import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().strip().split())
S = defaultdict(lambda : False)
result = 0

for i in range(N) :
    tmp = input().strip()
    S[tmp] = True

for j in range(M):
    tmp = input().strip()
    if S[tmp] :
        result += 1

print(result)