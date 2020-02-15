import sys
N = int(sys.stdin.readline())
pay = []
dp = [0] * (N+1)
for i in range(N):
    pay.append(list(map(int, sys.stdin.readline().split())))
pay.append([0,0])
for i in range(N+1):
    dp[i] = max(dp[i], dp[i-1])
    if i + pay[i][0] <= N:
        dp[i+pay[i][0]] = max(dp[i] + pay[i][1], dp[i+pay[i][0]])
print(dp[-1])