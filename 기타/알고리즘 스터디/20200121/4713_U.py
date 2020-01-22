import sys
import copy
month = [31,28,31,30,31,30,31,31,30,31,30,31]
N = int(sys.stdin.readline())
days = []
for i in range(N):
    days.append(list(map(int, sys.stdin.readline().split())))

for day in days:
    if day[0] < 3:
        day[0] = 3
        day[1] = 1
    elif day[2] > 12:
        day[0] = 11
        day[1] = 30

days.sort()
before = [3, 1]
tmp = [0,0]
count = 0
maxSum = 0
for day in days:
    if (day[0] == before[0] and day[1] <= before[1]) or (day[0] <before[0]):

        if (day[2] == tmp[0] and day[3] > tmp[1]) or day[2]>tmp[0]:
            tmp[0] = day[2]
            tmp[1] = day[3]
        if day[2] ==12:
            count += 1
            break
    else:
        count += 1
        before = copy.deepcopy(tmp)
        if (day[0] == before[0] and day[1] <= before[1]) or (day[0] <before[0]):
            if (day[2] == tmp[0] and day[3] > tmp[1]) or day[2]>tmp[0]:
                tmp[0] = day[2]
                tmp[1] = day[3]
            if day[2] == 12:
                count += 1
                break
        maxSum = 0
        if tmp[0] <= day[0] and tmp[1] < day[1]:
            print(0)
            exit(0)
if tmp[0]<12:
    print(0)
else:
    print(count)
