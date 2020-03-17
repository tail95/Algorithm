import sys
sys.setrecursionlimit(50000)
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0:
        break
    
    maps = []
    visited = [[False]*w for _ in range(h)]
    answer = 0

    for _ in range(h):
        maps.append(list(map(int, sys.stdin.readline().split())))
    
    def dfs(x, y):
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)

    for i in range(h):
        for j in range(w):
            if maps[i][j] and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                answer += 1
    print(answer)