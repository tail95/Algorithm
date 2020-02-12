import sys
answer = 0
N, P = map(int, sys.stdin.readline().split())
guitar = {}
for i in range(N):
    n, p = map(int, sys.stdin.readline().split())
    if n in guitar.keys():
        tmp = guitar[n][-1]
        if tmp < p:
            answer += 1
            guitar[n].append(p)
        elif tmp > p:
            while True:
                guitar[n].pop()
                answer += 1
                if not guitar[n]:
                    break
                tmp = guitar[n][-1]
                if tmp <= p:
                    break
            if tmp != p:
                guitar[n].append(p)
                answer += 1
    else:
        guitar[n] = [p]
        answer += 1
print(answer)
