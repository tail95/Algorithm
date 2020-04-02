def swap(board, l):
    result = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            result[j][i] = board[i][j]
    return result

def solution(board, moves):
    answer = 0
    l = len(board)
    board = swap(board, l)
    
    stack = [] 
    
    for m in moves:
        m = m - 1
        for i in range(l):
            if board[m][i] != 0:
                if stack and stack[-1] == board[m][i]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[m][i])            
                board[m][i] = 0
                break

    return answer