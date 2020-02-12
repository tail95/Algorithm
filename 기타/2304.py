import sys
N = int(sys.stdin.readline())
answer = 0
sticks = []
for _ in range(N):
    sticks.append(list(map(int, sys.stdin.readline().split())))
sticks.sort()

my = max(map(lambda x:x[1], sticks))
mx = 0
mxList = []
for i, stick in enumerate(sticks):
    if stick[1] == my:
        mxList.append(i)
maxin = 0
minin = 987654321
for m in mxList:
    if minin >= m:
        minin = m
    if maxin<= m:
        maxin = m
diff = sticks[maxin][0] - sticks[minin][0] + 1
prev = sticks[0]
left = 0
for i in range(1, minin + 1):
    if prev[1] < sticks[i][1]:
        left += (sticks[i][0] - prev[0]) * prev[1]
        prev = sticks[i]
prev = sticks[-1]
right = 0
for j in range(len(sticks) - 2 , maxin - 1, -1):
    if prev[1] < sticks[j][1]:
        right += ((prev[0]+1) - (sticks[j][0]+1)) * prev[1]
        prev = sticks[j]
mid = diff * my
print(left + right + mid)