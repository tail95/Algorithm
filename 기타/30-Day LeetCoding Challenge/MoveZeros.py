class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        while left < right:
            while nums[left] != 0:
                if left > right or left >= len(nums) - 1:
                    break
                left += 1
            while nums[right] == 0 or right <= 0:
                if left > right:
                    break
                right -= 1
            nums.append(nums.pop(left))
        return nums
