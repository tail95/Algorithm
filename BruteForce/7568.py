num = int(input())
people = []
for i in range(num):
    wh = list(map(int, input().split()))
    people.append(wh)
answer = []
for i in range(len(people)):
    tmp = 1
    for j in range(len(people)):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                tmp += 1
    print(tmp, end = " ")
