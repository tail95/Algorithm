import sys
T = int(sys.stdin.readline())
dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(6, 101):
    dp[i] = dp[i-5] + dp[i-1]

while T:
    N = int(sys.stdin.readline())
    print(dp[N])
    T -= 1
