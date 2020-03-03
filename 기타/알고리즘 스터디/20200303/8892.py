import sys

def check(word):
    ret = True
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            ret = False
            break
        left += 1
        right -= 1
    # for i in range(lw//2):
    #     if word[i] != word[lw-1-i]:
    #         ret = False
    #         break    
    return ret

T = int(sys.stdin.readline())
while T:
    k = int(sys.stdin.readline())
    words = []
    for _ in range(k):
        words.append(sys.stdin.readline().split())
    flag = False
    for i in range(k):
        if flag:
            break
        for j in range(k):
            if i != j:
                t1 = words[i][0] + words[j][0]
                if check(t1):
                    print(t1)
                    flag = True
                    break
                t2 = words[j][0] + words[i][0]
                if check(t2):
                    print(t2)
                    flag = True
                    break
    if not flag:
        print("0")
    T -= 1