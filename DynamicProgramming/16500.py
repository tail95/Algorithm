import sys
S = sys.stdin.readline()
N = int(sys.stdin.readline())
flag = False
sub = []
dp = [False for _ in range(len(S)-1)]
for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    if S.startswith(tmp):
        dp[len(tmp) - 1] = True
    sub.append(tmp)
for i in range(len(S)-1):
    if dp[i]:
        for s in sub:
            if S[i+1:].startswith(s):
                dp[i+len(s)] = True
# print(dp)
print("1") if dp[-1] else print("0")




# aaaabaa
# 2
# aa
# b
# =>1

# aaaaabaa
# 2
# aa
# b
# =>0

# aaaaaaaaaa
# 2
# aaaa
# aaa
# =>1

