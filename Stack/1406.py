import sys
words = list(sys.stdin.readline().rstrip())
sub = list()
n = int(sys.stdin.readline())
for i in range(n):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == "L" and words:
        sub.append(words.pop())
    elif order[0] == "D" and sub:
        words.append(sub.pop())
    elif order[0] == "B" and words:
        words.pop()
    elif order[0] == "P":
        words.append(order[1])
# while sub:
#     words.append(sub.pop())
# print("".join(words))
print("".join(words + sub[::-1]))  # 리스트를 역순으로 출력함으로써 stack에서 pop 하듯이 동작

# 시간 초과로 인해 문제 풀이에 어려움
# 반복문 내에서 input() 대신 sys.sdin.readLine() 사용
# list의 특정 인덱스 값을 제거 하는 것은 O(n)시간이 걸림 <-> pop() 은 O(1) // pop(index)는 O(n)