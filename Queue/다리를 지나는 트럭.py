from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.reverse()
    onBridge = deque([0 for _ in range(bridge_length)])
    sumOnBridge = 0
    while truck_weights:
        front = onBridge.popleft()    
        sumOnBridge -= front
        if sumOnBridge + truck_weights[-1] <= weight:
            truck = truck_weights.pop()
            onBridge.append(truck)
            sumOnBridge += truck
        else:
            onBridge.append(0)
        # print(onBridge)
        # print(truck_weights)
        answer += 1
    answer+=bridge_length
    return answer


# print(solution(5, 10, [5]))    # 6
# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100,100,[10]))
# print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))

# 내장 함수 sum을 사용하면 시간 초과 (전체 deque에 대해 실행되므로)
# 직접 다리위에 올라간 트럭들의 중량합을 더하고 빼서 구함(단순 덧셈)