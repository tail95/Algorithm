import sys

def dfs(x, y, color, mapping):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not isvisited[nx][ny] and mapping[nx][ny] == color:
            isvisited[nx][ny] = 1
            dfs(nx, ny, color, mapping)

n = int(input())
maps = []

for i in range(n):
    maps.append(sys.stdin.readline().rstrip())
colorBlindmaps=[]
for ma in maps:
    colorBlindmaps.append(ma.replace("R","G"))

normal = 0
isvisited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        color = maps[i][j]
        if not isvisited[i][j]:
            dfs(i, j, color, maps)
            normal += 1

colorBlind = 0
isvisited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        color = colorBlindmaps[i][j]
        if not isvisited[i][j]:
            dfs(i, j, color, colorBlindmaps)
            colorBlind+= 1

print(str(normal) + " " + str(colorBlind))