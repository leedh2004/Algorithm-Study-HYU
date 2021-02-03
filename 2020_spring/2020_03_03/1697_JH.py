#dfs 재귀로 짜볼랬는데 도저히 못하겠음 ㅎ ㅠ

# import collections
# N, K = map(int,input().split())

# def bfs(time):
#     global N
#     global K
#     q = collections.deque()
#     q.append(N)
#     count = 0

#     while q:
#         x = q.popleft()
#         if x == K :
#             return time[x]
        
#         for i in [x+1,x-1,x*2]:
#             if i>=0 and i<=100000 and time[i] == 0 :
#                 q.append(i)
#                 time[i] += time[x]+1

# time = [0]*100001
# print(bfs(time))