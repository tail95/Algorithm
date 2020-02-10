N, K = map(int, input().split())
dp = [[i]+[0]*(K-1) for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1,K):
        if i > j:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 10007
print(dp[N][K-1])
