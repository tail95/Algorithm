import sys
from collections import deque    
answer = 0
n = int(sys.stdin.readline())
connect = int(sys.stdin.readline())
visited = [False for _ in range(n)]
computers = [[0]*n for _ in range(n)]
for i in range(connect):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    computers[x-1][y-1] = 1
    computers[y-1][x-1] = 1
# print(computers)
q = deque()
q.append(0)
visited[0] = True
while q:
    front = q.popleft()
    # print(front)
    for i in range(n):
        if computers[front][i] and not visited[i] :
            visited[i] = True
            q.append(i)
            answer += 1
print(answer)



# bfs로 풀이함 
# 0번째 방문을 visited처리 하지않아 틀림
