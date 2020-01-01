import sys
n = int(sys.stdin.readline())
memebers = []
for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    memebers.append([i, int(age), name])

memebers.sort(key = lambda x: (x[1], x[0]))
for member in memebers:
    print(str(member[1]) + " " + str(member[2]))


# 값이 같을 경우 들어온 순서대로 정렬하기 때문에
# sort함수의 key함수에 x[1](나이값)으로 우선 정렬을 한후
# x[0](인덱스값)으로 재정렬 
# lambda x : x[1] 만 해도 정렬됨