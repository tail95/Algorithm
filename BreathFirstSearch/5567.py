import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
friends = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a][b] = 1
    friends[b][a] = 1

inviteds = [1]
queue = deque()
for i in range(n+1):
    if friends[1][i] == 1 and i not in inviteds:
        inviteds.append(i)
        queue.append(i)
while len(queue):
    front = queue.popleft()
    for i in range(n+1):
        if friends[front][i] == 1 and i not in inviteds:
            inviteds.append(i)

print(len(inviteds)-1)