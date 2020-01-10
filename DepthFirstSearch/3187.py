import sys
sys.setrecursionlimit(100000)
r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(input())

visited = [[False]*c for _ in range(r)]

def dfs(x, y, k, v):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    if maps[x][y] == "k":
        k+=1
    elif maps[x][y] == "v":
        v+=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < r and 0 <= ny < c and not visited[nx][ny] and maps[nx][ny] != "#":
            visited[nx][ny] = True
            k,v = dfs(nx,ny,k,v)
    return (k,v)
totalV = totalK = 0

for i in range(r):
    for j in range(c):
        if not visited[i][j] and maps[i][j] != "#":
            k=v=0
            visited[i][j] = True
            k, v = dfs(i,j,k,v)
            if k <= v:
                totalV += v
            else:
                totalK += k
print(str(totalK) + " " + str(totalV))


# python으로 DFS를 구현하면 재귀호출이 반복된다.
# sys.setrecursionrlimite을 수정하자!!!! 