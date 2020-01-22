import sys
n = int(sys.stdin.readline())
numbers = []
heights = []
answer = []
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
for i, num in enumerate(numbers):
    heights.append([i+1,num])
heights.reverse()

for counter, h in enumerate(heights):
    move = counter - h[1]
    answer.insert(move, h[0])
answer.reverse()
print(*answer)

# N = int(input())
# lh = [-1] + list(map(int, input().split()))
# print(lh)
# order = []
# for i in range(N, 0, -1):
#     order.insert(lh[i], i)
# print(order)