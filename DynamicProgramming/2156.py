import sys
n = int(sys.stdin.readline())
grapes = []
dp = [0 for _ in range(n)]
for i in range(n):
    grapes.append(int(sys.stdin.readline()))
try:
    dp[0] = grapes[0]
    dp[1] = grapes[0] + grapes[1]
    dp[2] = grapes[2] + max(grapes[0], grapes[1])
    dp[3] = max(grapes[0]+grapes[1], grapes[0]+grapes[2]) + grapes[3]
except:
    print(max(dp))
    exit(0)
for i in range(4, n):
    dp[i] = max(grapes[i-1]+max(dp[i-3],dp[i-4]), dp[i-2]) + grapes[i]
print(max(dp))

# import sys
# n = int(input())
# dp=[0 for x in range(n)]
# wine=[0]*n

# for x in range(n):

#     wine[x]=int(sys.stdin.readline().strip())
#     if x==0:
#         dp[x]=wine[x]

#     elif x==1:
#         dp[x]=wine[x]+dp[x-1]

#     elif x==2:
#         dp[x]=max(wine[x-2]+wine[x],wine[x-1]+wine[x],wine[x-2]+wine[x-1])
#     else:
#         dp[x]=max(dp[x-3]+wine[x]+wine[x-1],dp[x-2]+wine[x])
#         dp[x]=max(dp[x],dp[x-1])

# print(dp)