import sys
sys.setrecursionlimit(50000)

visited = [False for i in range(201)]
def dfs(n, computers, x):
    for i in range(n):
        if i!=x and computers[x][i] and not visited[i]:
            visited[i] = True
            dfs(n, computers, i)

def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] and not visited[j]:
                visited[j] = True
                dfs(n, computers, j)
                answer+=1
    return answer

print(solution(3, [[1,1,0],[1,1,0],[0,0,1]]))
print(solution(3, [[1,1,0],[1,1,1],[0,1,1]]))