import sys
N = int(sys.stdin.readline())
conferences = []
for _ in range(N):
    conferences.append(list(map(int, sys.stdin.readline().split())))
conferences.sort(key=lambda x: [x[1], x[0]])
answer = 0
prev = -1
for conf in conferences:
    if conf[0] >= prev:
        prev = conf[1]
        answer += 1
print(answer)