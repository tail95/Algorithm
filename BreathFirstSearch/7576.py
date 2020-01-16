import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatos = []
for i in range(N):
    tomatos.append(list(map(int, sys.stdin.readline().split())))

q = deque()
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            q.append((i, j))
while q:
    frontX, frontY = q.popleft()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = frontX + dx[i]
        ny = frontY + dy[i]
        if 0 <= nx < N and 0 <= ny < M and tomatos[nx][ny] == 0:
            tomatos[nx][ny] = max(tomatos[frontX][frontY] + 1, tomatos[nx][ny])
            q.append((nx,ny))

tCount = 0
tMax = 0
for t in tomatos:
    tCount += t.count(0)
    tMax = max(tMax, max(t))
if tCount>0:
    print(-1)
else:
    print(tMax - 1)

# 기존풀이: 1 상하 좌우로 1로 만듦 // 매 루프마다 1인것을 체크해 queue에 추가 ( 시간 소요 많음)
# 해결: 토마토의 거리를 계산해 거리 값을 계산 후 max값으로 계산 