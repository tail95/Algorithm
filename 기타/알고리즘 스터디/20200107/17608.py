import sys
answer = 1
n = int(sys.stdin.readline())
sticks = []
for i in range(n):
    sticks.append(int(sys.stdin.readline().rstrip()))
last = sticks[-1]
sticks.reverse()
for stick in sticks:
    if stick > last:
        last = stick
        answer += 1
print(answer)
