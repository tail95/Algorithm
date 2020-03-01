import sys
sys.setrecursionlimit(50000)
N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
answer = []

def dfs(li, add):
    li.append(add)
    length = len(li)
    if length == M:
        if li not in answer:
            # answer.append(li)
            print(*li)
        return
    if length < M:
        for number in numbers:
            dfs(li[:length], number)

for number in numbers:
    dfs([], number)

## 다른 방법
# def c(k,n,m):
#     if (k == m):
#         print(*res)
#         return
#     else:
#         for i in range(n):
#             res[k] = arr[i]
#             c(k+1,n,m)

# n, m = map(int,input().split())
# arr = range(1, n+1)
# res = [0] * m
# c(0,n,m)