import sys
n = int(sys.stdin.readline())
answer = 0
for i in range(n):
    word = sys.stdin.readline().rstrip()
    alphaChecker = []
    flag = True
    prev = word[0]
    for w in word[1:]:
        if w != prev:
            alphaChecker.append(prev)
        if w in alphaChecker:
            flag = False
        
        prev = w
    if flag:
        answer += 1
print(answer)