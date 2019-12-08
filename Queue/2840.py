n, k = map(int, input().split())
words = "?"*n
idx = 0
for i in range(k):
    count, word = input().split()
    idx = idx - (int(count) % n)
    if idx < 0:
        idx += n

    if words[idx] != "?" and words[idx] != word:   # 다른 문자가 같은 인덱스에 들어갈 경우
        print("!")
        exit(0)
    words = words[:idx] + word + words[idx+1:]

for i in range(n):   # 중복이 있는 경우
    for j in range(i+1, n):
        if words[i] != "?" and words[i] == words[j]:
            print("!")
            exit(0)

for i in range(n):
    print(words[(i + idx) % n], end='')