import sys
input = sys.stdin.readline
from collections import deque
from bisect import bisect_left

class Node(object):
    def __init__(self):
        self.data = []
        self.children = {}

class Tree(object):
    def __init__(self):
        self.head = Node()

    def insert(self, info):
        curr_node = self.head
        for i in info[:-1] :
            if i not in curr_node.children :
                curr_node.children[i] = Node()
            curr_node = curr_node.children[i]
        curr_node.data.append(int(info[-1]))
        curr_node.data.sort()

    def search(self, query, node):
        curr_node = node
        query = deque(query)
        count = 0
        
        t = query.popleft()
        if not query :
            if t == '-':
                return len(curr_node.data)
            else :
                t = int(t)
                return (len(curr_node.data) - bisect_left(curr_node.data,t))
                

        if t == '-':
            for key in curr_node.children :
                try :
                    count += self.search(query, curr_node.children[key])
                except :
                    return 0
                    count += 0

        else :
            try :
                count += self.search(query, curr_node.children[t])
            except :
                return 0
                count += 0

        return count


    def bfs(self):
        q = deque()
        q.append(self.head)
        while q:
            for i in range(len(q)):
                t = q.popleft()
                print(t.children, t.data)
                for key in t.children :
                    q.append(t.children[key])
            print("------------------------")


def solution(info, query):
    answer = []
    candidate = Tree()


    for i in info :
        candidate.insert(list(i.split()))

    # candidate.bfs()

    for q in query :
        lan, field, exp, foodScore = q.split(' and ')
        condition = [ lan, field, exp, *foodScore.split() ]
        result = candidate.search(condition, candidate.head)
        answer.append(result)

    return answer


# 정답은 통과, 효율성은 전부 시간 초과, DT 만들어야 함 ??
# def solution(info, query):
#     answer = []
#     candidate = []

#     for i in info :
#         candidate.append(i.split())

#     for q in query :
#         lan, field, exp, foodScore = q.split(' and ')
#         condition = [ lan, field, exp, *foodScore.split() ]
#         result = 0

#         for can in candidate :
#             flag = True
#             for i in range(4) :
#                 if condition[i]!="-" and condition[i]!=can[i] :
#                     flag = False
#                     break
#             if flag :
#                 if int(condition[4]) > int(can[4]) :
#                     flag = False
#             if flag :
#                 result += 1

#         answer.append(result)

#     return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))