import sys
def init(n, m):
    dp = [[0]*(m+2) for _ in range(n+2)]
    return dp

T = int(sys.stdin.readline())
while T:
    answer = 0
    N, M = map(int, sys.stdin.readline().split())
    dp = init(N, M)
    for i in range(1, N+2):
        for j in range(1, M+2):
            if i == 1:
                dp[i][j] = j
            else:
                if i == j:
                    dp[i][j] = 1
                elif i < j:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[N][M])
    T -= 1
