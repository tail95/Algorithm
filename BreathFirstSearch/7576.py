import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatos = []
answer = 0
for i in range(N):
    tomatos.append(list(map(int, sys.stdin.readline().split())))

visited = [[False]*M for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1 and not visited[i][j]:
            q.append((i, j))
            visited[i][j] = True
while q:
    # print(q)
    frontX, frontY = q.popleft()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = frontX + dx[i]
        ny = frontY + dy[i]
        # print("nx: " + str(nx) + " ny: " + str(ny))
        if 0 <= nx < N and 0 <= ny < M and tomatos[nx][ny] == 0 and not visited[nx][ny]:
            # print("#"*30)
            tomatos[nx][ny] = max(tomatos[frontX][frontY] + 1, tomatos[nx][ny])
            q.append((nx,ny))
# print(tomatos)
tCount = 0
tMax = 0
for t in tomatos:
    tCount += t.count(0)
    tMax = max(tMax, max(t))
if tCount>0:
    print(-1)
else:
    print(tMax - 1)