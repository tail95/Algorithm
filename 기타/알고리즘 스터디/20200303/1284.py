import sys
numbers = [4,2,3,3,3,3,3,3,3,3]
while True:
    N = sys.stdin.readline().rstrip()
    if int(N) == 0:
        break
    answer = 0
    for num in N:
        answer += numbers[int(num)]
    answer += len(N) + 1
    print(answer)
