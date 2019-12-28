import sys
import queue
n, m = map(int, sys.stdin.readline().split())
maze = []
dist = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
for i in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

q=queue.Queue()
q.put((0, 0))
dist[0][0]=1
visited[0][0] = True
while q: 
    i, j=q.get()
    if i==n-1 and j==m-1:
        break
    dx=[-1, 0, 1, 0]
    dy=[0, -1, 0, 1]
    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] and not visited[nx][ny]:
            visited[nx][ny]=True
            q.put((nx, ny))
            dist[nx][ny]=dist[i][j]+1

print(dist[n-1][m-1])
