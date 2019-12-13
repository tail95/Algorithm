import sys
sys.setrecursionlimit(100000)

def dfs(x, y, result):
    result = result + 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0 <= nx < n and 0 <= ny < m and trash[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            result += dfs(nx, ny, 0)
    return result

n, m, k = map(int, sys.stdin.readline().rstrip().split())
trash = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
answer = 0

for i in range(k):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    trash[x-1][y-1] = 1

for i in range(n):
    for j in range(m):
        if trash[i][j] and not visited[i][j]:
            visited[i][j] = True
            answer = max(answer, dfs(i,j,0))
print(answer)

# 변화값인 nx, ny에 대해서 dfs를 실행했어야 되는데 
# 생각없이 i, j 로 실행하면서 계산착오 발생
# nx, ny 정할때도 함수인자인 x,y가 아닌 i,j로 해서 ;;