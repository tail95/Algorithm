import sys
N = int(sys.stdin.readline())
xy = []
for _ in range(N):
    xy.append(list(map(int, sys.stdin.readline().split())))
xy.sort(key = lambda x: (x[0], x[1]))
for tmp in xy:
    print(*tmp, sep=" ")