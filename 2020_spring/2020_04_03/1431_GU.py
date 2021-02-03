import sys
import copy
#import re

N = int(sys.stdin.readline())

serial = []

for i in range(N):
    ser = sys.stdin.readline().rstrip()
    nums = [int(s) for s in ser if s.isdigit()]
    serial.append([ser,sum(nums)])
    nums.clear()
serial.sort(key = lambda x: (len(x[0]),x[1],x[0]))

for i in range(len(serial)):
    print(serial[i][0])
"""
serial.sort(key = lambda x: len(x[0])  
change_index =[0,] #when len is changed
for i in range(N-1):
    if len(serial[i][0]) != len(serial[i+1][0]):
        change_index.append(i+1)
if change_index[len(change_index)-1] != len(serial)-1:
    change_index.append(len(serial)-1)
#print(change_index)
for i in range(len(change_index)-1):
    start = change_index[i]
    end = change_index[i+1]
    if end-start != 1:
        nl = serial[start:end+1]
        nl.sort(key = lambda x: x[1])
        for j in range(start,end+1):
            serial[j] = nl[j-start]

same_index =[] #when len is changed
for i in range(N-1):
    if len(serial[i][0]) == len(serial[i+1][0]) and serial[i][1]==serial[i+1][1]:
        same_index.append(i)
        same_index.append(i+1)
same_index = list(set(same_index))

packet = []
tmp = []
if(same_index):
    v = same_index.pop(0)
    tmp.append(v)

while(len(same_index)>0 and same_index):

	vv = same_index.pop(0)

	if v+1 == vv:
		tmp.append(vv)
		v = vv

	else:
		packet.append(tmp)
		tmp = []
		tmp.append(vv)
		v = vv
packet.append(tmp)    # packet 부터 리스트에서 연속된 수의 리스트 담은 리스트 - packet

for i in range(len(packet)):
    tmp = packet[i]
    if len(tmp) == 0:
        break
    if len(tmp) == 1:
        continue
    start = tmp[0]
    end = tmp[len(tmp)-1]
    nl = serial[start:end+1]
    nl.sort()
    for j in range(start,end+1):
        serial[j] = nl[j-start]
"""
#for i in range(len(serial)):
#    print(serial[i][0])

""" 처음 시도한 것 
check_list =[] #start, end, start, end   which ones have same len
for i in range(N-1):
    if len(serial[i]) == len(serial[i+1]):
        check_list.append(i)
        for i in range(N-1):
            if len(serial[i]) != len(serial[i+1]):
                check_list.append(i)
                break
            elif i==N-2 and len(serial[i]) == len(serial[i+1]):
                check_list.append(N-1)

for i in range(len(check_list)//2):
    start = check_list[i]
    end = check_list[i+1]

    newSorted = ['0']*(start-end+1)
    sums =[0]*(start-end+1)
    for j in range(start,end+1):
        nums = [int(s) for s in serial[j].split() if s.isdigit()]
        sums[j-start] = sum(nums)
"""