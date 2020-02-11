import sys
answer = 0
N = int(sys.stdin.readline())
ropes = []
for i in range(N):
    ropes.append(int(sys.stdin.readline()))
ropes.sort(reverse=True)
for i in range(1, N+1):
    answer = max(answer, ropes[i-1]*i)
print(answer)