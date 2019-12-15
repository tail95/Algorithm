import sys
sys.setrecursionlimit(50000)

region = []
answer = 0
n = int(input())
for i in range(n):
    region.append(list(map(int, sys.stdin.readline().rstrip().split())))

def dfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and region[nx][ny] > t:
            visited[nx][ny] = True
            dfs(nx, ny)


for t in range(max(map(max, region))):
    tmp = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if region[i][j] > t and not visited[i][j]:
                tmp += 1
                visited[i][j] = True
                dfs(i, j)
    answer = max(answer, tmp)
print(answer)


# dfs 호출에서 dfs 이후에 visited를 True로 만들어서 오류(서순)
# 문제를 제대로 읽을 것!
# 물이 주어진 n이 아니라 차오르는 동안의 최댓값을 구하는문제인데 그냥 n에 대해서만 구함

