import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
while T:
    N, M = map(int, sys.stdin.readline().rstrip().split())
    prior = map(int, sys.stdin.readline().rstrip().split())
    counter = 0
    dq = deque(prior)
    idx = M
    while dq:
        maximum = max(dq)
        if maximum == dq[0]:
            dq.popleft()
            counter+=1
            if idx == 0:
                print(counter)
                break
            idx-=1
        else:
            dq.append(dq.popleft())
            idx-=1
            if idx < 0:
                idx += len(dq)
    T-=1
