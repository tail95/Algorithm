while True:
    try:
        n, k = map(int, input().split())
        answer = n
        while True:
            div = n // k
            n = n % k + div
            answer += div
            if n < k:
                break
        print(answer)
    except:
        exit()