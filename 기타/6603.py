# from itertools import combinations
# import sys
# while True:
#     numbers = list(map(int, sys.stdin.readline().split()))
#     if numbers == [0]:
#         break
#     for tmp in list(combinations(numbers[1:], 6)):
#         print(*tmp)
#     print()


#  DFS를 이용한 방법
# def lotto(x, y):
#     print(ans)
#     if y == 6:
#         for i in range(6):
#             print("{0} ".format(ans[i]), end='')
#         print()
#         return
#     for i in range(x, k):
#         ans[y] = a[i]
#         lotto(i+1, y+1)

# while True:
#     a = list((map(int, input().split())))
#     k = a[0]
#     if k == 0:
#         break
#     a = a[1:]
#     ans = [0 for _ in range(k)]
#     lotto(0, 0)
#     print()