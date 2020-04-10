class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minimum = self.stack[0]
        for i in range(1, len(self.stack)):
            if self.stack[i] < minimum:
                minimum = self.stack[i]
        return minimum


# # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.pop()
# obj.push(3)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class Node:
    def __init__(self, val):
        self.value = val
        self.minValue = None
        self.next = None
    def __str__(self):
        return str(self.value)


class MinStack:        
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:
        n = Node(x)
        if self.head == None:
            minValue = x
        else:
            minValue = min(self.head.minValue, x)
        n.minValue = minValue
        n.next = self.head
        self.head = n
        
        
    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.value

    def getMin(self) -> int:
        return self.head.minValue