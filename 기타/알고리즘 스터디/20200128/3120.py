a, b = map(int, input().split())
dp = [1,2,3,2,1,2,3,3,2,1]
d = [0]
for i in range(4):
    for dyp in dp:
        d = d + [dyp+i]
        # d.extend(dyp+i)
if b < a :
    a,b=b,a
diff = b - a     

print(d[diff])
# temp = [-1,1,-5,5,-10,10]

# for i in range(41):
#     tmp = 987654321
#     for t in temp:
#         if 0 <= i+t < 41:
#             tmp = min(tmp, dp[i+t] + 1)
#     dp[i] = tmp

    
# print(dp)