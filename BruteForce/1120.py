A, B = input().split()
minScore = 987654321
for i in range(len(B) - len(A) + 1):
    tmp = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            tmp += 1
    minScore = min(minScore, tmp)
print(minScore)
