# import sys
# t = int(sys.stdin.readline())
# while t:
#     n = int(sys.stdin.readline())
#     numbers = []
#     flag = True
#     for i in range(n):
#         numbers. append(sys.stdin.readline().rstrip())
#     numbers.sort(key=lambda x: len(x))

#     ln = len(numbers)
#     for i in range(ln - 1):
#         for j in range(i+1, ln):
#             if numbers[j].startswith(numbers[i]):
#                 flag=False
#     if flag:
#         print("YES")
#     else:
#         print("NO")
#     t-=1
###### 시간 초과 #####

# 시간 초과 개선 
import sys
t = int(sys.stdin.readline())
while t:
    n = int(sys.stdin.readline())
    numbers = []
    flag = True
    for i in range(n):
        numbers. append(sys.stdin.readline().rstrip())
    numbers.sort()    # 문자열로 정열 

    ln = len(numbers)
    for i in range(ln - 1):
        if len(numbers[i]) == len(numbers[i+1]):
            continue
        # 다음 인덱스 값에 포함되면 일관성 X
        # 문자열 순서로 정렬하기 때문에 가능 
        if numbers[i+1].startswith(numbers[i]):
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")
    t -= 1
