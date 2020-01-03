from collections import deque
N, K = map(int, input().split())
circularQ = deque([i for i in range(1,N+1)])
counter = 1 
output = []
while circularQ:
    if counter % K == 0:
        output.append(circularQ.popleft())
    else:
        circularQ.append(circularQ.popleft())
    counter += 1
print("<", end="")
for i, out in enumerate(output):
    if i != N - 1:
        print(str(out) + ",", end=" ")
    else:
        print(out, end="")
print(">")
