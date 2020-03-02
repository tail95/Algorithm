import sys
N = int(sys.stdin.readline())
maps = []
dp = [[0]*N for _ in range(N)]

for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        k = maps[i][j]
        if i+k < N:
            dp[i+k][j] = dp[i+k][j] + dp[i][j]
        if j+k < N:
            dp[i][j+k] = dp[i][j+k] + dp[i][j]
print(dp[-1][-1])