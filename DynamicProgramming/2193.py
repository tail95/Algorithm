n = int(input())
dp = [0 for i in range(n+1)]
if n == 1 or n == 2:  #  n이 1이나 2로 들어올때
    print(1)
    exit(0)
dp[1] = 1   # 할당하면 런타임 에러 발생
dp[2] = 1
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])


# 기본적인 피보나치 형식의 문제여서 간단히 풀었는데
# # 계속 런타임 에러가 떠서 당황했는데
# # C++의 경우 longlong형을 써야되지만 파이썬은 노상관이긴함
# # 결국 할당할때 문제 발생하는것으로 파악