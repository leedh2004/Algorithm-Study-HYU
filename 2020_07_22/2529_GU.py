import sys

def dfs(v):
	global d, visit,stack
	for i in range(len(d[v])):
		next_v = d[v][i]
		if visit[next_v] == 0:
			visit[next_v] = 1
			dfs(next_v)
	stack.append(v)

def dfs2(v):
	global d, visit2,stack2
	for i in range(len(d[v])):
		next_v = d[v][i]
		if visit2[next_v] == 0:
			visit2[next_v] = 1
			dfs2(next_v)
	stack2.append(v)

k = int(sys.stdin.readline())
A = list(sys.stdin.readline().split())
d = dict()
stack = [] # for maximum
stack2 = [] # for minimum
visit = [0 for _ in range(k+1)] # for max
visit2 = [0 for _ in range(k+1)] # for min
for i in range(k+1):
	d[i] = []
for i in range(k):
	if A[i] == '>':
		d[i+1].append(i)
	else: d[i].append(i+1)

for i in range(k+1):
	if visit[i] == 0:
		visit[i] = 1
		dfs(i)
for i in range(k,-1,-1):
	if visit2[i] == 0:
		visit2[i] = 1
		dfs2(i)
stack.reverse()
stack2.reverse()

max_idx = 9-k
min_idx = 0
max_ = [0 for _ in range(k+1)]
min_ = [0 for _ in range(k+1)]
for i in range(k+1):
	idx = stack[i]
	idx2 = stack2[i]
	max_[idx] = max_idx
	min_[idx2] = min_idx
	max_idx += 1
	min_idx += 1

max_ = map(str,max_)
min_ = map(str,min_)
print(''.join(max_))
print(''.join(min_))



"""def dfs(v):
	global d, visit,stack
	for i in range(len(d[v])):
		next_v = d[v][i]
		if visit[next_v] == 0:
			visit[next_v] = 1
			dfs(next_v)
	stack.append(v)

k = int(sys.stdin.readline())
A = list(sys.stdin.readline().split())
d = dict()
stack = []
visit = [0 for _ in range(k+1)]
for i in range(k+1):
	d[i] = []
for i in range(k):
	if A[i] == '>':
		d[i+1].append(i)
	else: d[i].append(i+1)
for i in range(k+1):
	if visit[i] == 0:
		visit[i] = 1
		dfs(i)
stack.reverse()
print(stack)
max_idx = 9-k
#min_idx = 0
max_ = [0 for _ in range(k+1)]
#min_ = [0 for _ in range(k+1)]
for i in range(k+1):
	idx = stack[i]
	max_[idx] = max_idx
	#min_[idx] = min_idx
	max_idx += 1
	#min_idx += 1
max_ = map(str,max_)
#min_ = map(str,min_)
print(''.join(max_))
#print(''.join(min_))
min_ = [i for i in range(k+1)]
min_ = map(str,min_)
min_comb = list(map(''.join,itertools.permutations(min_)))
min_comb.sort()
min_len = len(min_comb)
min_res = [True for _ in range(min_len)]
for i in range(k):
	if A[i] == '>':
		for j in range(min_len):
			y = min_comb[j]
			if min_res[j] == True and y[i] <= y[i+1]:
				min_res[j] = False
	elif A[i] == '<':
		for j in range(min_len):
			y = min_comb[j]
			if min_res[j] == True and y[i] >= y[i+1]:
				min_res[j] = False
for i in range(min_len):
	if min_res[i] == True:
		print(min_comb[i])
		break
"""
"""
import itertools
k = int(sys.stdin.readline())
A = list(sys.stdin.readline().split())
max_ = [i for i in range(9-k,10)]
min_ = [i for i in range(k+1)]
max_ = map(str,max_)
min_ = map(str,min_)
max_comb = list(map(''.join,itertools.permutations(max_)))
max_comb.sort()
min_comb = list(map(''.join,itertools.permutations(min_)))
min_comb.sort()
max_len = len(max_comb)
min_len = len(min_comb)
max_res = [True for _ in range(max_len)]
min_res = [True for _ in range(min_len)]
for i in range(k):
	if A[i] == '>':
		for j in range(max_len):
			x = max_comb[j]
			if max_res[j] == True and x[i] <= x[i+1]:
				max_res[j] = False
		for j in range(min_len):
			y = min_comb[j]
			if min_res[j] == True and y[i] <= y[i+1]:
				min_res[j] = False
	elif A[i] == '<':
		for j in range(max_len):
			x = max_comb[j]
			if max_res[j] == True and x[i] >= x[i+1]:
				max_res[j] = False
		for j in range(min_len):
			y = min_comb[j]
			if min_res[j] == True and y[i] >= y[i+1]:
				min_res[j] = False

for i in range(max_len-1,-1,-1):
	if max_res[i] == True:
		print(max_comb[i])
		break
for i in range(min_len):
	if min_res[i] == True:
		print(min_comb[i])
		break
"""
"""weight = [0 for _ in range(k+1)]
maximum = [0 for _ in range(k+1)]
minimum = [0 for _ in range(k+1)]
weight[0] = k//2
for i in range(k):
	if A[i] == '<':
		weight[i+1] = weight[i] + 1 
	else:
		weight[i+1] = weight[i] - 1

b = min(weight)
c = max(weight)

max_idx = 9-k
min_idx = 0

for i in range(b,c+1):
	li = [j for j, value in enumerate(weight) if value == i]
	for k in range(len(li)):
		minimum[li[k]] = min_idx
		min_idx += 1
		maximum[li[len(li)-k-1]] = max_idx
		max_idx += 1
maximum = map(str,maximum)
minimum = map(str,minimum)
print(''.join(maximum))
print(''.join(minimum))"""