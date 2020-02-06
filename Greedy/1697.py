from collections import deque
N, K = map(int, input().split())
visited = [False] * 100001
q = deque()
q.append([N])
answer = 0
while len(q):
    tmp = q.popleft()
    if K in tmp:
        break
    ext = []
    for i in range(len(tmp)):
        if 0 <= tmp[i]-1 <=100000 and not visited[tmp[i]-1]:
            ext += [tmp[i]-1]
            visited[tmp[i]-1] = True
        if  0 <= tmp[i]+1 <=100000 and not visited[tmp[i]+1]:
            ext += [tmp[i]+1]
            visited[tmp[i]+1] = True
        if 0 <= tmp[i]*2 <=100000 and not visited[tmp[i]*2]:
            ext += [tmp[i]*2]
            visited[tmp[i]*2] = True
    q.append(ext)
    answer += 1
print(answer)

# if not visited[tmp[i]*2] and 0 <= tmp[i]*2 <=100000:
# if 0 <= tmp[i]*2 <=100000 and not visited[tmp[i]*2]:
# 같은 조건문이라도 앞부분을 먼저 체크하기 때문에
# 위에 if문에서 RuntimeError가 발생한다.