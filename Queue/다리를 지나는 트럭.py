from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.reverse()
    onBridge = deque([0 for _ in range(bridge_length)])
    sumOnBridge = 0
    while truck_weights:
        if sumOnBridge + truck_weights[-1] <= weight:
            front = onBridge.popleft()
            sumOnBridge -= front
            truck = truck_weights.pop()
            onBridge.append(truck)
            sumOnBridge += truck
        else:
            front = onBridge.popleft()
            sumOnBridge -= front
            if front == 0 :
                onBridge.append(front)
            else:
                if sum(onBridge) + truck_weights[-1] <= weight:
                    truck = truck_weights.pop()
                    onBridge.append(truck)
                    sumOnBridge+=truck
                else:
                    onBridge.append(0)  
        # print(onBridge)
        # print(truck_weights)
        answer += 1
    answer+=bridge_length
    return answer


print(solution(5, 10, [5]))    # 6
print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))