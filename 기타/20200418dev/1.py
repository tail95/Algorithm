def solve(s,t):
    if s < t:
        s, t = t, s
    ret = s - t
    if ret > 5:
        ret = 10 - ret
    return ret
def solution(p,s):
    answer= 0
    for i in range(len(p)):
        source = int(p[i])
        target = int(s[i])
        answer += solve(source, target)
    return answer