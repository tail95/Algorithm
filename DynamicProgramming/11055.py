N = int(input())
numbers = [0] + list(map(int, input().split()))
dp = [[0]*2 for _ in range(N+1)]
for i in range(N+1):
    tmp = 0
    for j in range(i-1, 0, -1):
        if dp[j][0] > tmp and dp[j][1] < numbers[i]:
            tmp = dp[j][0]
    dp[i][0] = tmp + numbers[i]
    dp[i][1] = numbers[i]
# print(dp)
maxNum = 0
for d in dp:
    if d[0] > maxNum:
        maxNum = d[0]
print(maxNum)


# from copy import deepcopy
# N = int(input())
# numbers = list(map(int, input().split()))
# dp = deepcopy(numbers)
# answer = 0
# for i in range(N):
#     for j in range(0, i):
#         if numbers[i] > numbers[j]:
#             dp[i] = max(dp[j] + numbers[i], dp[i]);
#     answer = max(dp[i], answer)
# print(answer)
