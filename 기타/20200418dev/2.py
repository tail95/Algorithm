def solution(office, r, c, move):
    answer = 0
    answer += office[r][c]
    office[r][c] = 0
    direction = [[-1,0], [0,1], [1,0], [0,-1]]
    to = 0
    for m in move:
        if m == "go":
            dr, dc = direction[to][0], direction[to][1]
            if 0 <= r+dr < len(office) and 0<= c+dc < len(office) and office[r+dr][c+dc] != -1:
                r += dr
                c += dc
                answer += office[r][c]
                office[r][c] = 0
            else:
                continue
        elif m == "right":
            to += 1
            to %= 4
        elif m == "left":
            to -= 1
            to %= 4
            
    return answer