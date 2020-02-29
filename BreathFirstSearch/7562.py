import sys
from collections import deque
T = int(sys.stdin.readline())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
while T:
    I = int(sys.stdin.readline())
    chess = [[0]*I for _ in range(I)]
    visited = [[False]*I for _ in range(I)]
    start = list(map(int, sys.stdin.readline().split()))
    end = list(map(int, sys.stdin.readline().split()))
    answer = 0

    q = deque()
    q.append([start])
    visited[start[0]][start[1]] = True
    while q:
        positions = q.popleft()
        if end in positions:
            break
        tmp = []
        for pos in positions:
            for i in range(8):
                nx = pos[0] + dx[i]
                ny = pos[1] + dy[i]
                if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                    visited[nx][ny] = True
                    tmp.append([nx,ny])
        answer += 1
        q.append(tmp)
    print(answer)
    T -= 1