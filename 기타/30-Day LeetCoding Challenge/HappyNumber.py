import sys
sys.setrecursionlimit(50000)
class Solution:
    def __init__(self):
        self.happy = []
    def isHappy(self, n: int) -> bool:
        sumNum = 0
        while n:
            sumNum += (n % 10) ** 2
            n //= 10
        if sumNum == 1:
            return True
        if sumNum in self.happy:
            return False
        else:
            self.happy.append(sumNum)
            return self.isHappy(sumNum) 