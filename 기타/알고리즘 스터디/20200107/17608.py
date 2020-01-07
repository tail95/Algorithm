import sys
answer = 1
n = int(sys.stdin.readline())
sticks = []
for i in range(n):
    sticks.append(int(sys.stdin.readline().rstrip()))
last = sticks[-1]
sticks.reverse()
for stick in sticks:
    if stick > last:
        last = stick
        answer += 1
print(answer)

# 긴 막대기가 있으면 뒤에 있는 막대기가 안보이므로 
# 긴 막대기를 업데이트 해줘야됨