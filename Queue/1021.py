from collections import deque

N, M = map(int, input().split())
target = input().split()
numbers = []
for i in range(N):
    numbers.append(str(i + 1))
answer = 0
numbers = deque(numbers)
for i in range(M):
    # print(target[i])
    if numbers[0] == target[i]:
        numbers.popleft()
    else:
        target_number = numbers.index(target[i])
        back = len(numbers) - target_number
        if (target_number <= back):
            while (numbers[0] != target[i]):
                # print("left", end="\t")
                # print(numbers, end=' ')
                numbers.append(numbers.popleft())
                answer += 1
                # print(answer)
        else:
            while (numbers[0] != target[i]):
                # print("right", end="\t")
                # print(numbers, end=' ')
                numbers.appendleft(numbers.pop())
                answer += 1
                # print(answer)
        numbers.popleft()
print(answer)