class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        checkList = []
        for num in nums:
            if num in checkList:
                checkList.pop(checkList.index(num))
            else:
                checkList.append(num)
        return checkList[0]