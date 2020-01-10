dp = [1 for _ in range(70)]
dp[2]=2;dp[3]=4
for i in range(4, 70):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
n = int(input())
for _ in range(n):
    print(dp[int(input())])

# 점화식을 문제에서 보여주고있는 문제 Ez