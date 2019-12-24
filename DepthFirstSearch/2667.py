import sys
sys.setrecursionlimit(50000)
n = int(sys.stdin.readline())
maps = []
complex = 0
apartments = []

def dfs(x, y, count):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maps[nx][ny] == "1":
            visited[nx][ny] = True
            count = dfs(nx, ny, count)
    return count

for i in range(n):
    maps.append(sys.stdin.readline().rstrip())
visited = [[False] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == "1":
            complex += 1
            visited[i][j] = True
            apartments.append(dfs(i, j, 0))
print(complex)
for apart in sorted(apartments):
    print(apart)

# 문자열로 읽어들여서 숫자 1이 아닌 문자 "1" 로 체크하는데서 걸림
# 단지수를 카운트할 때 고민함