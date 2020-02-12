import sys

def dfs(start, next, li):
    if next == li[0]:
        return True
    if not visited[next]:
        tmp.append(next)
        visited[next] = True
        return dfs(start, nummaps[next][1], tmp)

N = int(sys.stdin.readline())
nummaps = [[i,0] for i in range(N+1)]
for i in range(1, N+1):
    nummaps[i][1] = int(sys.stdin.readline())
result = []
for i in range(1, N+1):
    flag = False
    visited = [False] * (N+1)
    tmp = []
    tmp.append(i)
    if dfs(i, nummaps[i][1], tmp):
        result += tmp
sett = list(set(result))
sett.sort()
print(len(sett))
print(*sett, sep="\n")

