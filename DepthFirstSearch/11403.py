import sys

def dfs(start):
    for i in range(N):
        if maps[start][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs(i)

N = int(sys.stdin.readline())
maps = []
result = [[0]*N for _ in range(N)]
for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    visited = [0] * N
    dfs(i)
    print(*visited)