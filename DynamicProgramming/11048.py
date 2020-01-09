import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
maps = []
dp = [[0] * M for _ in range(N)]
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))


for i in range(N):
    for j in range(M):
        up = left = diagonal =0
        if 0<i and 0< j:
            diagonal = dp[i-1][j-1]
        if 0<i:
            up = dp[i-1][j]
        if 0<j:
            left = dp[i][j-1]
        dp[i][j] = max([diagonal, up, left]) + maps[i][j];
print(dp[N-1][M-1])