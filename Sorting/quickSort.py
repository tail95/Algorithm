import random
from time import sleep
arr = [random.randint(1, 20) for _ in range(10)]
arr = [6, 5, 3, 1, 8, 7, 2, 4]


def quickSort(l, r):
    left = l
    right = r
    
    # pivot = random.randint(l, r)
    p = arr[l]
    print("l: " + str(l) + " r: " + str(r))
    while l < r:
        print(arr)
        while arr[l] <= p and l < r:
            l += 1
        if l<r:
            break
        while arr[r] >= p and l < r:
            r -= 1
        if l<r:
            break
        arr[l], arr[r] = arr[r], arr[l]
        sleep(1)
    arr[left], arr[l] = arr[left], arr[l]
    if left < l:
        quickSort(left, l - 1)
    if right > r:
        quickSort(l+1, right)


print("Before")
print(arr)
quickSort(0, len(arr)-1)
print("After")
print(arr)

