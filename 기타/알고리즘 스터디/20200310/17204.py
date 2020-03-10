import sys
N, K = map(int ,sys.stdin.readline().split())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

visited = [False] * N
flag = False
key = 0
answer = 0
while True:
    if(numbers[key] == K):
        answer += 1
        break
    if(visited[numbers[key]]):
        flag=True
        break
    else:
        key = numbers[key]
        visited[key] = True
        answer+= 1
if not flag:
    print(answer)
else:
    print(-1)