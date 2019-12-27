import sys
from collections import deque
sys.setrecursionlimit(50000)
N, M, V = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    fr, to = map(int, sys.stdin.readline().rstrip().split())
    graph[fr][to] = graph[to][fr] = 1

def dfs(vertex):
    visited[vertex] = True
    print(vertex, end= ' ')
    for i in range(len(graph[vertex])):
        if not visited[i] and graph[vertex][i]:
            visited[i] = True
            dfs(i)
    
def bfs(vertex):
    visited = [False for i in range(N+1)]
    q = deque()
    q.append(vertex)
    visited[vertex] = True
    while q:
        current = q.popleft()
        print(current, end= ' ')
        for i in range(len(graph[current])):
            if graph[current][i] and not visited[i]:
                q.append(i)
                visited[i]=True
            
visited = [False for i in range(N+1)]
dfs(V)
print()
bfs(V)