N = int(input())
lh = [-1] + list(map(int, input().split()))
order = []
for i in range(N, 0, -1):
    order.insert(lh[i], i)
print(*order)


# list의 insert함수를 활용하면됌 
# insert(index, value)
# print(*list, sep=" ") 리스트 출력법
