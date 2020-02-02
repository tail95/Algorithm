def solution(numbers):  
    if numbers.count(0)==len(numbers):
        return "0"
    num = list(map(str, numbers))
    num.sort(reverse=True)
    target = [[0]*2 for _ in range(len(num))]
    for i in range(len(num)):
        target[i][0] = num[i]
        target[i][1] = (str(num[i])*4)[:4]
    target.sort(key=lambda x:x[1], reverse=True)
    return answer