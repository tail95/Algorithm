import random
arr = [random.randint(1, 1000) for i in range(1000)]

def bubbleSort():
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

print("Before")
print(arr)
bubbleSort()
print("After")
print(arr)
