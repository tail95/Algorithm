N = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4, N+1, 2):
    dp[i] = dp[i-2] * 3 +2
    for j in range(4, i, 2):
        dp[i] += dp[i-j]*2 
print(dp[N])

# 3 x N 타일이기 때문에 홀수일 때는 타일을 채울 수 없다. 
# 또한, 짝수의 경우 n이 4이상일 때부터 특이 케이스가 2개씩 추가된다.
# 추가된 특이 케이스 전체에 대해 주고 (line 5 ==> +2) 
# 특이 케이스에 대해 dp를 또 적용해줘야된다.(line 7 ==> dp[i-j]*2)
