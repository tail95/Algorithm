import sys
heights = []
for _ in range(9):
    heights.append(int(sys.stdin.readline()))
sh = sum(heights)
flag = False
for i in range(len(heights) - 1):
    for j in range(i + 1, len(heights)):
        if sh - heights[i] - heights[j] == 100:
            a=i
            b=j
            flag = True
            break
    if flag:
        break
result = []
for k in range(len(heights)):
    if k == a or k == b:
        continue
    result.append(heights[k])
result.sort()
print(*result, sep="\n")
