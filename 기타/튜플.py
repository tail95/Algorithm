def solution(s):
    answer = []
    tmp = s[2:-2].split("},{")
    tup = []
    for t in tmp:
        tup.append(t.split(","))
    
    tup.sort(key = lambda x:len(x))
    for t in tup:
        check = list(map(int, t))
        for c in check:
            if c not in answer:
                answer.append(c)
    return answer