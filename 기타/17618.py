N = int(input())
answer = 0
for i in range(1, N+1):
    summ = 0
    tmp = i
    while tmp:
        summ += tmp % 10
        tmp = tmp // 10
    if i % summ == 0:
        answer += 1
print(answer)