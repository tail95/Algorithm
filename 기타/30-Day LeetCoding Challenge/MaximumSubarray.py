class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i]
            dp[i] = max(dp[i], dp[i] + dp[i-1])
        return max(dp)
