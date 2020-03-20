import sys
T = int(sys.stdin.readline())
dp = [[0]*3 for _ in range(100001)]
dp[1][0] = 1
dp[2][1] = 1
mod = 1000000009
for i in range(3):
    dp[3][i] = 1
for i in range(4, 100001):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % mod
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % mod
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % mod
while T:
    n = int(sys.stdin.readline())
    print(sum(dp[n]) % mod)
    T -= 1